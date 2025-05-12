# core_utils.py
from typing import Callable, Iterator, Tuple
# If you want to use ProcessorFn for type hinting the return type of linewise:
# from types1 import ProcessorFn, TaggedLine

# This definition of ProcessorFn is what types1.py provides:
# ProcessorFnDefinition = Callable[[Iterator[Tuple[str, str]]], Iterator[Tuple[str, str]]]


def linewise(
    # fn takes only the line_content (str) and returns a (output_tag, new_line_content) tuple
    fn_line_processor: Callable[[str], Tuple[str, str]],
) -> Callable[
    [Iterator[Tuple[str, str]]], Iterator[Tuple[str, str]]
]:  # Returns a full ProcessorFn
    """
    A decorator to adapt a simple line-processing function (which only cares about
    string content and outputs a single tagged line) to the full ProcessorFn signature.
    The input tag of the incoming TaggedLine is ignored by fn_line_processor.
    """

    def wrapped_processor(
        tagged_lines_iterator: Iterator[Tuple[str, str]],
    ) -> Iterator[Tuple[str, str]]:
        for _input_tag, line_content in tagged_lines_iterator:
            # The user's function `fn_line_processor` is called with just the content
            output_tag, processed_content = fn_line_processor(line_content)
            yield (output_tag, processed_content)

    return wrapped_processor


# Example of a linewise function that *is* aware of the input tag:
def tag_aware_linewise(
    # fn takes an (input_tag, line_content) tuple and returns an (output_tag, new_line_content) tuple
    fn_tagged_line_processor: Callable[[Tuple[str, str]], Tuple[str, str]],
) -> Callable[
    [Iterator[Tuple[str, str]]], Iterator[Tuple[str, str]]
]:  # Returns a full ProcessorFn
    """
    A decorator similar to linewise, but the provided function fn_tagged_line_processor
    receives the full (input_tag, line_content) tuple for each line.
    """

    def wrapped_processor(
        tagged_lines_iterator: Iterator[Tuple[str, str]],
    ) -> Iterator[Tuple[str, str]]:
        for input_tag, line_content in tagged_lines_iterator:
            # The user's function `fn_tagged_line_processor` is called with the full tagged line
            output_tag, processed_content = fn_tagged_line_processor(
                (input_tag, line_content)
            )
            yield (output_tag, processed_content)

    return wrapped_processor
