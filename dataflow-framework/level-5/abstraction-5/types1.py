# types1.py
from typing import Callable, Iterator, Tuple, Union

# ProcessorFn = Callable[[Iterator[str]], Iterator[str]] # Original
ProcessorFn = Callable[
    [Iterator[Tuple[str, str]]], Iterator[Tuple[str, str]]
]  # Modified - This is correct for the new design
Route = str
TaggedLine = Tuple[Route, str]  # (tag/route, line content)
Lines = Iterator[TaggedLine]  # Can be useful, but Iterator[TaggedLine] is more direct
