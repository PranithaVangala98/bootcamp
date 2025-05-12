from typing import Iterator


def add_line_number(lines: Iterator[str]) -> Iterator[str]:
    for i, line in enumerate(lines, 1):
        yield f"{i} : {line}"
