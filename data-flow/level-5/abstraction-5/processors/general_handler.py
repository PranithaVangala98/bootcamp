# processors/general_handler.py
from typing import Iterator, Tuple
from types1 import TaggedLine, Route


def format_and_output_general(
    tagged_lines_iterator: Iterator[TaggedLine],
) -> Iterator[TaggedLine]:
    """
    Formats general lines and yields them for final output.
    Input: Iterator of ("general", general_line_content)
    Output: Iterator of ("formatted_general", formatted_line_content)
    """
    for _input_tag, line_content in tagged_lines_iterator:  # _input_tag is "general"
        # The output tag "formatted_general" will be printed by cli.py
        # as it's not expected to be a key in processors_map (i.e., it's a terminal tag)
        yield ("formatted_general", f"INFO: {line_content}")
