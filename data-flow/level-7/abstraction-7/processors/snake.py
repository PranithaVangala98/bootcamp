from typing import Iterator, Tuple


def to_snakecase(lines: Iterator[Tuple[str, str]]) -> Iterator[Tuple[str, str]]:
    for route, line in lines:
        yield (route, line.lower().replace(" ", "_"))
