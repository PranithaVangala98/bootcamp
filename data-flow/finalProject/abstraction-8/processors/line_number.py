from typing import Iterator, Tuple


def add_line_number(lines: Iterator[Tuple[str, str]]) -> Iterator[Tuple[str, str]]:
    for i, (route, line) in enumerate(lines, 1):
        yield (route, f"{i} : {line}")
