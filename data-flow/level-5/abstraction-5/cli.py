# cli.py
import typer
from typing import Optional
# Removed List, Dict, Tuple if not directly used in this file's annotations after changes

from dotenv import load_dotenv
from pipeline import get_processors
from core import process_lines

load_dotenv()

app = typer.Typer()

# Define a conventional initial tag for raw input lines.
# The first processor in pipeline.yaml should listen to this tag.
INITIAL_ROUTE_TAG = "input"


@app.command()
def run(
    input_filename: str = typer.Option(..., "--input", "-i", help="Input filename"),
    output: Optional[str] = typer.Option(
        None, "--output", "-o", help="Output filename"
    ),
    config: str = typer.Option(
        "pipeline.yaml", "--config", "-c", help="Path to YAML config file"
    ),
):
    """
    Runs the processing pipeline on the input file based on the YAML configuration.
    """
    try:
        with open(input_filename, "r") as f:
            # Create a list of lines directly. process_lines will take an iterator.
            lines = [line.rstrip("\n") for line in f]
    except FileNotFoundError:
        print(f"Error: Input file '{input_filename}' not found.")
        raise typer.Exit(code=1)
    except Exception as e:
        print(f"Error reading input file '{input_filename}': {e}")
        raise typer.Exit(code=1)

    try:
        # processors_map: Dict[Route, ProcessorFn]
        # routing_config_from_yaml: Dict[Route, List[Route]] (this is no longer used for dispatch by core.py)
        processors_map, _routing_config_from_yaml = get_processors(config)
    except FileNotFoundError:
        print(f"Error: Config file '{config}' not found.")
        raise typer.Exit(code=1)
    except (
        ValueError,
        ImportError,
    ) as e:  # Catch errors from pipeline loading/resolving
        print(f"Error loading pipeline configuration or processors: {e}")
        raise typer.Exit(code=1)

    # Get the iterator of TaggedLine results
    result_iterator = process_lines(iter(lines), processors_map, INITIAL_ROUTE_TAG)

    try:
        if output:
            with open(output, "w") as f:
                for route_tag, line_content in result_iterator:
                    f.write(f"[{route_tag}] {line_content}\n")
            print(f"Processing complete. Output written to '{output}'.")
        else:
            for route_tag, line_content in result_iterator:
                print(f"[{route_tag}] {line_content}")
            print("Processing complete. Output printed to console.")

    except Exception as e:
        # Catch errors during processing or writing output
        print(f"An error occurred during processing or writing output: {e}")
        # Potentially log more details or provide partial output if appropriate
        raise typer.Exit(code=1)


if (
    __name__ == "__main__"
):  # Although main.py is your entry, good practice for cli files
    app()
