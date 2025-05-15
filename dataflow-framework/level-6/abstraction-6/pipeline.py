# pipeline.py
import os
import importlib
import yaml
from types1 import (
    ProcessorFn,
)  # Assuming types1.py is in the same directory or accessible path
from typing import (
    List,
    Dict,
    Tuple,
)  # Keep Tuple if load_pipeline_config still returns it

default_mode = os.getenv("MY_KEY")  # This seems unused, but left as is.


def load_pipeline_config(
    path: str = "pipeline.yaml",
) -> Tuple[
    Dict[str, str], Dict[str, List[str]]
]:  # Returns processor types and routing map
    """Loads the pipeline configuration: processor types and routing rules."""
    try:
        with open(path, "r") as f:
            config = yaml.safe_load(f)
        if config is None or "pipeline" not in config:
            raise ValueError(
                f"Invalid YAML: 'pipeline' key missing or file empty in '{path}'."
            )

        pipeline_config = config.get("pipeline", [])
        if not isinstance(pipeline_config, list):
            raise ValueError(f"Invalid YAML: 'pipeline' should be a list in '{path}'.")

        processors_types: Dict[str, str] = {}
        routing_rules: Dict[str, List[str]] = {}

        for i, step in enumerate(pipeline_config):
            if not isinstance(step, dict):
                raise ValueError(
                    f"Invalid YAML: Pipeline step at index {i} is not a dictionary in '{path}'."
                )
            if "route" not in step or "type" not in step:
                raise ValueError(
                    f"Invalid YAML: Pipeline step at index {i} must have 'route' and 'type' in '{path}'."
                )

            route_name = step["route"]
            processor_type = step["type"]
            if not isinstance(route_name, str) or not isinstance(processor_type, str):
                raise ValueError(
                    f"Invalid YAML: 'route' and 'type' must be strings for step at index {i} in '{path}'."
                )

            processors_types[route_name] = processor_type

            # routes_to is optional, and its interpretation has changed.
            # It's loaded here but not used by the new core.py for dispatch.
            routes_to = step.get("routes_to", [])
            if not isinstance(routes_to, list):
                raise ValueError(
                    f"Invalid YAML: 'routes_to' must be a list for route '{route_name}' in '{path}'."
                )
            routing_rules[route_name] = routes_to

        return processors_types, routing_rules
    except FileNotFoundError:
        raise FileNotFoundError(f"Pipeline config file '{path}' not found.")
    except yaml.YAMLError as e:
        raise ValueError(f"Invalid YAML in pipeline config '{path}': {e}")


def resolve_processor(import_path: str) -> ProcessorFn:
    """Resolves a processor's import path to a callable function."""
    try:
        module_path, func_name = import_path.rsplit(".", 1)
        module = importlib.import_module(module_path)
        processor = getattr(module, func_name)
        if not callable(processor):
            # Ensure it's the correct ProcessorFn type if you had stricter checking
            raise TypeError(f"Resolved object '{import_path}' is not callable.")
        return processor
    except (
        ImportError,
        AttributeError,
        ValueError,
    ) as e:  # ValueError for rsplit if '.' not found
        raise ImportError(f"Error loading processor '{import_path}': {e}")


def get_processors(
    config_path: str = "pipeline.yaml",
) -> Tuple[Dict[str, ProcessorFn], Dict[str, List[str]]]:
    """
    Gets the processors map and routing configuration from the pipeline config.

    Returns:
        A tuple containing:
        - A dictionary of processors (route_tag -> processor_function).
        - A dictionary of original routing rules from YAML (route_tag -> list_of_destination_tags).
          (Note: The new core.py primarily uses processor output tags for dispatch).
    """
    try:
        processor_types_map, routing_config = load_pipeline_config(config_path)
    except (
        FileNotFoundError,
        ValueError,
    ) as e:  # Catch errors from load_pipeline_config
        # Re-raise or handle, for cli.py to catch top-level
        raise e

    resolved_processors: Dict[str, ProcessorFn] = {}
    for route_tag, import_path_str in processor_types_map.items():
        try:
            resolved_processors[route_tag] = resolve_processor(import_path_str)
        except ImportError as e:  # Catch errors from resolve_processor
            # Provide context about which processor failed
            print(
                f"[ERROR] Failed to resolve processor for route '{route_tag}' (path: '{import_path_str}'): {e}"
            )
            # Depending on desired behavior, you might skip, or raise to stop all processing
            raise ImportError(f"Skipping processor for route '{route_tag}': {e}") from e

    return resolved_processors, routing_config
