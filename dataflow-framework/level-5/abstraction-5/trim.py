from typing import Iterator, Tuple


def trim(lines: Iterator[str]) -> Iterator[Tuple[str, str]]:
    for line in lines:
        yield ("default", line.strip())
