# # trim.py
# from typing import Iterator, Tuple


# # Modified trim function to accept (tag, content) tuples
# # This aligns with how core.py passes data to processors.
# def trim(tagged_lines: Iterator[Tuple[str, str]]) -> Iterator[Tuple[str, str]]:
#     """
#     Processor function that takes an iterator of (tag, line_content) tuples,
#     trims whitespace from the content, and yields (new_tag, trimmed_content) tuples.
#     It currently ignores the input tag and always outputs with the tag "default".
#     """
#     # Iterate through the incoming tagged lines
#     for input_tag, line_content in tagged_lines:
#         # Process the line content (e.g., trim whitespace)
#         trimmed_content = line_content.strip()

#         # Yield the processed line with a new tag.
#         # Here, we are hardcoding the output tag to "default".
#         # A more complex processor might determine the output tag based on the content
#         # or the input_tag.
#         output_tag = "default"
#         yield (output_tag, trimmed_content)


# # If you had other utility functions in this file, they would go here.
# # For example, if you wanted to use the tag_aware_linewise decorator from core_utils:
# # from core_utils import tag_aware_linewise
# #
# # @tag_aware_linewise
# # def simple_trim_line(input_tag: str, line_content: str) -> Tuple[str, str]:
# #     # This function receives the tuple, but the decorator handles the iteration
# #     return ("default", line_content.strip())


# trim.py
from typing import Iterator, Tuple


# This function now correctly accepts an iterator of (tag, line_content) tuples
# as passed by core.py to processors.
def trim(tagged_lines: Iterator[Tuple[str, str]]) -> Iterator[Tuple[str, str]]:
    """
    Processor function that takes an iterator of (tag, line_content) tuples,
    trims whitespace from the content, and yields (new_tag, trimmed_content) tuples.
    It currently ignores the input tag and always outputs with the tag "default".
    """
    # Iterate through the incoming tagged lines, unpacking the tuple
    for input_tag, line_content in tagged_lines:
        # Process the line content (e.g., trim whitespace)
        # This operation should be safe for most text lines.
        try:
            trimmed_content = line_content.strip()
        except Exception as e:
            # Added basic error handling within the processor itself
            # to see if the strip() operation is the source of failure.
            print(f"Error processing line '{line_content}': {e}")
            # Re-raising the exception or yielding a specific error tag
            # would depend on desired error handling within the pipeline.
            # For now, we'll let the core.py error handling catch it,
            # but this print helps debug if strip() is the issue.
            raise  # Re-raise the exception so core.py's error handling is triggered

        # Yield the processed line with a new tag.
        # The 'default' tag means core.py will look for a processor
        # configured for the 'default' route in pipeline.yaml, or
        # yield it as terminal output if no such processor exists.
        output_tag = "default"
        yield (output_tag, trimmed_content)


# If you had other utility functions in this file, they would go here.
# For example, if you wanted to use the tag_aware_linewise decorator from core_utils:
# from core_utils import tag_aware_linewise
#
# @tag_aware_linewise
# def simple_trim_line(input_tag: str, line_content: str) -> Tuple[str, str]:
#     # This function receives the tuple, but the decorator handles the iteration
#     return ("default", line_content.strip())
