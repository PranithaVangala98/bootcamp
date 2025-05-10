from core_utils import linewise


@linewise
def to_snakecase(line: str) -> str:
    return line.lower().replace(" ", "_")
