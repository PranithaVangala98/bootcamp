from types1 import ProcessorFn
from typing import Callable, Iterator


def linewise(fn: Callable[[str], str]) -> ProcessorFn:
    def wrapped(lines: Iterator[str]) -> Iterator[str]:
        for line in lines:
            yield fn(line)

    return wrapped
