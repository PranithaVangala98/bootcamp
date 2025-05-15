from typing import Callable, Iterator

ProcessorFn = Callable[[Iterator[str]], Iterator[str]]
