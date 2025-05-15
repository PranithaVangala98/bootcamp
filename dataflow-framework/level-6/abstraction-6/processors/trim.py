# processors/trim.py
from typing import Iterator, Tuple
from types1 import TaggedLine, Route  # Optional: for type hinting clarity


# Conforms to ProcessorFn: Callable[[Iterator[Tuple[str, str]]], Iterator[Tuple[str, str]]]
def process_trimmed_lines(
    tagged_lines_iterator: Iterator[TaggedLine],
) -> Iterator[TaggedLine]:
    """
    Trims whitespace from lines and tags them for the next stage (e.g., classification).
    Input: Iterator of (input_tag, line_content)
    Output: Iterator of ("needs_classification", trimmed_line_content)
    """
    # input_tag for the very first processor will be INITIAL_ROUTE_TAG (e.g., "input")
    for _input_tag, line_content in tagged_lines_iterator:
        yield ("needs_classification", line_content.strip())
