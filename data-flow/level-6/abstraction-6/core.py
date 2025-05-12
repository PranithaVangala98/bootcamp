# core.py
from typing import Iterator, List, Tuple, Dict, Set
from types1 import ProcessorFn, TaggedLine, Route
from collections import defaultdict


def process_lines(
    initial_lines_content: Iterator[str],
    processors_map: Dict[Route, ProcessorFn],
    initial_route_tag: Route = "input",  # Convention for the first tag of raw input lines
) -> Iterator[TaggedLine]:
    """
    Processes lines through a DAG of processors based on tagged routing.
    Lines are routed based on the output tags from processors.
    If a tag does not correspond to a known processor, the line is yielded as terminal output.
    """
    pending_data: Dict[Route, List[TaggedLine]] = defaultdict(list)

    # Tag initial lines with the initial_route_tag
    for line_content in initial_lines_content:
        pending_data[initial_route_tag].append((initial_route_tag, line_content))

    # Queue of routes that have data and a corresponding processor
    routes_to_process_queue: List[Route] = []
    if pending_data[initial_route_tag] and initial_route_tag in processors_map:
        routes_to_process_queue.append(initial_route_tag)
    elif pending_data[
        initial_route_tag
    ]:  # Initial tag has data but no processor, yield directly
        for item in pending_data.pop(initial_route_tag):
            yield item

    known_processing_routes = set(processors_map.keys())

    # Iteratively process routes
    # Keeps track of routes processed in the current "wave" to manage queue additions correctly
    processed_in_current_wave: Set[Route] = set()

    while routes_to_process_queue:
        current_route = routes_to_process_queue.pop(0)  # FIFO processing of routes
        processed_in_current_wave.add(current_route)

        # Get lines for the current route processor, clearing them from pending_data for this route
        lines_for_processor_input = list(pending_data.pop(current_route, []))

        if not lines_for_processor_input:
            # Should not happen if route was added to queue only when it had data,
            # but as a safeguard.
            continue

        if current_route in processors_map:
            processor = processors_map[current_route]
            # Processor takes Iterator[Tuple[input_tag, line_content]]
            # and yields Iterator[Tuple[output_tag, processed_content]]
            processed_output_iterator = processor(iter(lines_for_processor_input))

            for output_tag, processed_line_content in processed_output_iterator:
                new_tagged_line = (output_tag, processed_line_content)

                if output_tag in known_processing_routes:
                    # This line is routed to another known processor
                    pending_data[output_tag].append(new_tagged_line)
                    # Add the output_tag to the queue if it's not already there
                    # and hasn't been processed in the current wave (for complex cyclic graphs, though DAGs are typical)
                    if (
                        output_tag not in routes_to_process_queue
                        and output_tag not in processed_in_current_wave
                    ):
                        routes_to_process_queue.append(output_tag)
                else:
                    # This output_tag does not map to any known processor,
                    # so consider the line terminal for this tag and yield it.
                    yield new_tagged_line
        else:
            # This should ideally not be hit if routes_to_process_queue only contains known_processing_routes.
            # However, if lines were somehow tagged for a route without a processor and ended up here.
            for tagged_line in lines_for_processor_input:  # Yield them as is
                yield tagged_line

        # If the current queue is empty, it's the end of a "wave" of processing.
        # Replenish the queue with any routes that now have pending data and a processor.
        if not routes_to_process_queue:
            processed_in_current_wave.clear()  # Reset for the next wave
            for r_key, r_data_list in pending_data.items():
                # If a route has data, maps to a processor, and isn't already queued
                if (
                    r_data_list
                    and r_key in known_processing_routes
                    and r_key not in routes_to_process_queue
                ):
                    routes_to_process_queue.append(r_key)

            # If queue is still empty, check for any remaining data in pending_data
            # that is tagged for routes without processors (final terminal outputs).
            if not routes_to_process_queue:
                for r_key in list(
                    pending_data.keys()
                ):  # Iterate over keys (copy) as we might pop
                    if pending_data[r_key] and r_key not in known_processing_routes:
                        for item in pending_data.pop(r_key, []):  # Pop and yield
                            yield item
