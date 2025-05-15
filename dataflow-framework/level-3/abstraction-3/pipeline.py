import os
import importlib
import yaml
from types1 import ProcessorFn
from typing import List

default_mode = os.getenv("MY_KEY")


def load_pipeline_config(path: str = "pipeline.yaml") -> List[str]:
    with open(path, "r") as f:
        config = yaml.safe_load(f)
    return [step["type"] for step in config.get("pipeline", [])]


def resolve_processor(import_path: str) -> ProcessorFn:
    module_path, func_name = import_path.rsplit(".", 1)
    module = importlib.import_module(module_path)
    return getattr(module, func_name)


# def uppercase_processor(line: str) -> str:
#     return line.upper()


# def snakecase_processor(line: str) -> str:
#     return line.lower().replace(" ", "_")


def get_processors(config_path: str = "pipeline.yaml") -> List[ProcessorFn]:
    paths = load_pipeline_config(config_path)
    return [resolve_processor(path) for path in paths]
