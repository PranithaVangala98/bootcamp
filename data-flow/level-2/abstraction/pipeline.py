import os
from types1 import ProcessorFn

default_mode = os.getenv("MY_KEY")


def uppercase_processor(line: str) -> str:
    return line.upper()


def snakecase_processor(line: str) -> str:
    return line.lower().replace(" ", "_")


def get_processors(mode: str) -> list[ProcessorFn]:
    if mode is None:
        mode = default_mode

    if mode == "uppercase":
        return [uppercase_processor]
    elif mode == "snakecase":
        return [snakecase_processor]
    else:
        return []  # No processing
