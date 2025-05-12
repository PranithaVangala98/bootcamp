# types1.py
from typing import Callable, Iterator, Tuple, List

# Define the type for a trace: a list of route names encountered by a line
Trace = List[str]

# Define the TaggedLine to include the trace history
TaggedLine = Tuple[str, str, Trace]  # (route/tag, line content, trace history)

# Processor functions still receive and yield only the (route, line_content) part.
# The 'core.py' will manage the trace history around the processor calls.
ProcessorFn = Callable[[Iterator[Tuple[str, str]]], Iterator[Tuple[str, str]]]

# For clarity, define Route as str
Route = str
