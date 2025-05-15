from types1 import ProcessorFn
from typing import Iterator, List


def process_lines(lines: Iterator[str], processors: List[ProcessorFn]) -> Iterator[str]:
    for processor in processors:
        lines = processor(lines)
    return lines
