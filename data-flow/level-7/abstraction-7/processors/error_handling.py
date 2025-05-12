# processors/error_handling.py
from typing import Iterator, Tuple
from types1 import TaggedLine, Route

error_count = 0  # Global state; be mindful if concurrency is ever introduced


def count_and_archive_errors(
    tagged_lines_iterator: Iterator[TaggedLine],
) -> Iterator[TaggedLine]:
    """
    Counts errors, archives them, and yields a processed tagged line.
    Input: Iterator of ("errors", error_line_content)
    Output: Iterator of ("archived_error", confirmation_message)
    """
    global error_count
    for _input_tag, line_content in tagged_lines_iterator:  # _input_tag is "errors"
        error_count += 1
        try:
            with open("errors.log", "a") as f:
                f.write(f"[Error #{error_count}] {line_content}\n")
            # Yield a new tag indicating completion for this line, or for further processing if any
            yield ("archived_error", f"Archived Error #{error_count}: {line_content}")
        except IOError as e:
            # Handle file writing error, maybe yield a different tag or print to stderr
            yield (
                "archiving_failed",
                f"Failed to archive error: {line_content} due to {e}",
            )
