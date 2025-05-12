# core.py
import time
from typing import Iterator, List, Tuple, Dict, Set
from types1 import ProcessorFn, TaggedLine, Route, Trace
from collections import defaultdict

import observability_store  # Import the new observability store


def process_lines(
    initial_lines_content: Iterator[str],
    processors_map: Dict[Route, ProcessorFn],
    initial_route_tag: Route = "input",
    trace_enabled: bool = False,  # New parameter for tracing
) -> Iterator[TaggedLine]:
    """
    Processes lines through a DAG of processors based on tagged routing.
    Lines are routed based on the output tags from processors.
    If a tag does not correspond to a known processor, the line is yielded as terminal output.
    Adds metrics and tracing.
    """
    # Pending data now holds the full TaggedLine (route, content, trace)
    pending_data: Dict[Route, List[TaggedLine]] = defaultdict(list)

    # Initialize metrics for all known processors
    for proc_name in processors_map.keys():
        observability_store.initialize_metrics_for_processor(proc_name)

    # Tag initial lines with the initial_route_tag and an initial trace
    for line_content in initial_lines_content:
        initial_trace: Trace = [initial_route_tag] if trace_enabled else []
        pending_data[initial_route_tag].append(
            (initial_route_tag, line_content, initial_trace)
        )
        # Update metrics for initial input if initial_route_tag is a processor
        if initial_route_tag in processors_map:
            observability_store.update_metrics_received(initial_route_tag)

    routes_to_process_queue: List[Route] = []
    if pending_data[initial_route_tag] and initial_route_tag in processors_map:
        routes_to_process_queue.append(initial_route_tag)
    elif pending_data[
        initial_route_tag
    ]:  # Initial tag has data but no processor, yield directly
        for item in pending_data.pop(initial_route_tag):
            if trace_enabled:
                # For terminal lines, add to traces store
                observability_store.add_trace(
                    item[1], item[2]
                )  # content, final trace (which contains the terminal tag)
            yield item

    known_processing_routes = set(processors_map.keys())

    processed_in_current_wave: Set[Route] = set()

    while routes_to_process_queue:
        current_route = routes_to_process_queue.pop(0)
        processed_in_current_wave.add(current_route)

        # Get lines for the current route processor, clearing them from pending_data
        # These are the (route, content, trace) tuples
        lines_for_processor_input: List[TaggedLine] = list(
            pending_data.pop(current_route, [])
        )

        if not lines_for_processor_input:
            continue

        if current_route in processors_map:
            processor = processors_map[current_route]

            start_time = time.perf_counter()
            try:
                # Pass only the (route, content) part to the actual processor
                processor_input_for_fn = [
                    (tag, content) for tag, content, _trace in lines_for_processor_input
                ]

                processed_output_iterator = processor(iter(processor_input_for_fn))
                processing_duration_ms = (time.perf_counter() - start_time) * 1000
                observability_store.update_metrics_time(
                    current_route, processing_duration_ms
                )

                emitted_count_for_current_processor = 0

                # To correctly map output lines back to their original traces,
                # we assume a 1:1 relationship for simplicity in this context.
                # A robust solution for n:m transformations would require unique line IDs.
                # For now, we zip the input lines (with traces) with the processor's outputs.
                processed_lines_with_original_traces = zip(
                    lines_for_processor_input, processed_output_iterator
                )

                for (
                    _input_tag,
                    _original_content,
                    original_trace,
                ), (
                    output_tag,
                    processed_line_content,
                ) in processed_lines_with_original_traces:
                    emitted_count_for_current_processor += 1
                    new_trace: Trace = (
                        original_trace + [output_tag] if trace_enabled else []
                    )
                    new_tagged_line: TaggedLine = (
                        output_tag,
                        processed_line_content,
                        new_trace,
                    )

                    if output_tag in known_processing_routes:
                        # This line is routed to another known processor
                        pending_data[output_tag].append(new_tagged_line)
                        # Update metrics for the next processor (line received)
                        observability_store.update_metrics_received(output_tag)
                        if (
                            output_tag not in routes_to_process_queue
                            and output_tag not in processed_in_current_wave
                        ):
                            routes_to_process_queue.append(output_tag)
                    else:
                        # This output_tag does not map to any known processor,
                        # so consider the line terminal for this tag and yield it.
                        if trace_enabled:
                            observability_store.add_trace(
                                processed_line_content, new_trace
                            )
                        yield new_tagged_line

                observability_store.update_metrics_emitted(
                    current_route, emitted_count_for_current_processor
                )

            except Exception as e:
                error_message = str(e)
                observability_store.update_metrics_error(current_route)
                # Add error to store. Try to get a representative line for context.
                representative_line = (
                    lines_for_processor_input[0][1]
                    if lines_for_processor_input
                    else None
                )
                observability_store.add_processor_error(
                    current_route, error_message, representative_line
                )

                # Yield lines that caused errors with a special tag, preserving content and trace
                for _tag, content, trace in lines_for_processor_input:
                    error_tag = f"{current_route}_failed"  # Tag indicating failure at this route
                    final_trace = trace + [error_tag] if trace_enabled else []
                    if trace_enabled:
                        observability_store.add_trace(content, final_trace)
                    yield (error_tag, content, final_trace)

        else:
            # Route has no processor, yield directly.
            for item in lines_for_processor_input:
                if trace_enabled:
                    observability_store.add_trace(
                        item[1], item[2] + [item[0]]
                    )  # trace should already contain current route
                yield item

        if not routes_to_process_queue:
            processed_in_current_wave.clear()
            for r_key, r_data_list in pending_data.items():
                if (
                    r_data_list
                    and r_key in known_processing_routes
                    and r_key not in routes_to_process_queue
                ):
                    routes_to_process_queue.append(r_key)

            if not routes_to_process_queue:
                # No more active routes, yield any remaining pending data as terminal outputs
                for r_key in list(pending_data.keys()):
                    if pending_data[r_key]:  # and r_key not in known_processing_routes:
                        for item in pending_data.pop(r_key):
                            if trace_enabled:
                                observability_store.add_trace(
                                    item[1],
                                    item[2],  # trace already contains terminal tag
                                )
                            yield item
