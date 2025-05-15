# processors/warning_handler.py
from typing import Iterator, Tuple
from types1 import TaggedLine, Route

warning_tally = 0  # Global state


def tally_and_log_warnings(
    tagged_lines_iterator: Iterator[TaggedLine],
) -> Iterator[TaggedLine]:
    """
    Tallies warnings and yields a processed tagged line.
    Input: Iterator of ("warnings", warning_line_content)
    Output: Iterator of ("tallied_warning", confirmation_message)
    """
    global warning_tally
    for _input_tag, line_content in tagged_lines_iterator:  # _input_tag is "warnings"
        warning_tally += 1
        # This processor could just perform an action (like logging to a specific place)
        # and/or yield a line for further general output or specific tracking.
        # For example, log to a warnings.log
        try:
            with open("warnings.log", "a") as f:
                f.write(f"[Warning #{warning_tally}] {line_content}\n")
            yield (
                "tallied_warning",
                f"Tallied Warning #{warning_tally}: {line_content}",
            )
        except IOError as e:
            yield (
                "warning_logging_failed",
                f"Failed to log warning: {line_content} due to {e}",
            )
