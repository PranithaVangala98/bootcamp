# processors/tagging.py
from typing import Iterator, Tuple
from types1 import TaggedLine, Route


def classify_and_tag_lines(
    tagged_lines_iterator: Iterator[TaggedLine],
) -> Iterator[TaggedLine]:
    """
    Classifies lines based on content and tags them for specific handlers.
    Input: Iterator of ("needs_classification", line_content)
    Output: Iterator of ("errors", line), ("warnings", line), or ("general", line)
    """
    for (
        _input_tag,
        line_content,
    ) in tagged_lines_iterator:  # _input_tag is "needs_classification"
        line_upper = line_content.upper()  # For case-insensitive matching
        if "ERROR" in line_upper:
            yield ("errors", line_content)
        elif "WARNING" in line_upper:
            yield ("warnings", line_content)
        else:
            yield ("general", line_content)
