import os
import importlib
import yaml
from types1 import ProcessorFn
from typing import List

default_mode = os.getenv("MY_KEY")


def load_pipeline_config(path: str = "pipeline.yaml") -> List[str]:
    try:
        with open(path, "r") as f:
            config = yaml.safe_load(f)
        return [step["type"] for step in config.get("pipeline", [])]
    except FileNotFoundError:
        raise FileNotFoundError(f"Pipeline config file '{path}' not found.")
    except yaml.YAMLError as e:
        raise ValueError(f"Invalid YAML in pipeline config: {e}")


def resolve_processor(import_path: str) -> ProcessorFn:
    try:
        module_path, func_name = import_path.rsplit(".", 1)
        module = importlib.import_module(module_path)
        processor = getattr(module, func_name)
        if not callable(processor):
            raise TypeError(f"Resolved object '{func_name}' is not callable.")
        return processor
    except (ImportError, AttributeError, ValueError) as e:
        raise ImportError(f"Error loading processor '{import_path}': {e}")


# def uppercase_processor(line: str) -> str:
#     return line.upper()


# def snakecase_processor(line: str) -> str:
#     return line.lower().replace(" ", "_")


def get_processors(config_path: str = "pipeline.yaml") -> List[ProcessorFn]:
    import_paths = load_pipeline_config(config_path)
    processors = []
    for path in import_paths:
        try:
            processor = resolve_processor(path)
            processors.append(processor)
        except Exception as e:
            print(f"[ERROR] Skipping processor '{path}': {e}")
    return processors
