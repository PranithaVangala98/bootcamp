# cli.py
import typer
from typing import Optional, Iterator  # Added Iterator
import threading
import time  # For sleep

from dotenv import load_dotenv
from pipeline import get_processors
from core import process_lines
from types1 import TaggedLine  # Import TaggedLine for type hinting result_iterator
import observability_store  # Import the store
from dashboard import start_dashboard_server  # Import the function to start dashboard

load_dotenv()

app = typer.Typer()

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
    dashboard: bool = typer.Option(
        False, "--dashboard", "-d", help="Run the web dashboard"
    ),  # New flag for dashboard
    trace: bool = typer.Option(
        False, "--trace", "-t", help="Enable execution tracing for lines"
    ),  # New flag for tracing
):
    """
    Runs the processing pipeline on the input file based on the YAML configuration.
    """
    # Reset observability store for a clean run, useful during development
    observability_store.reset_observability_store()

    # --- Start Dashboard if enabled ---
    dashboard_thread: Optional[threading.Thread] = None
    if dashboard:
        typer.echo("Starting web dashboard at http://0.0.0.0:8000...")
        dashboard_thread = threading.Thread(target=start_dashboard_server, daemon=True)
        dashboard_thread.start()
        time.sleep(1)  # Give the server a moment to start

    try:
        with open(input_filename, "r") as f:
            lines = [line.rstrip("\n") for line in f]
    except FileNotFoundError:
        typer.echo(f"Error: Input file '{input_filename}' not found.")
        raise typer.Exit(code=1)
    except Exception as e:
        typer.echo(f"Error reading input file '{input_filename}': {e}")
        raise typer.Exit(code=1)

    try:
        processors_map, _routing_config_from_yaml = get_processors(config)
    except FileNotFoundError:
        typer.echo(f"Error: Config file '{config}' not found.")
        raise typer.Exit(code=1)
    except (
        ValueError,
        ImportError,
    ) as e:
        typer.echo(f"Error loading pipeline configuration or processors: {e}")
        raise typer.Exit(code=1)

    # Get the iterator of TaggedLine results, passing the trace_enabled flag
    result_iterator: Iterator[TaggedLine] = process_lines(
        iter(lines), processors_map, INITIAL_ROUTE_TAG, trace_enabled=trace
    )

    try:
        if output:
            with open(output, "w") as f:
                for (
                    route_tag,
                    line_content,
                    _trace_history,
                ) in result_iterator:  # Unpack trace_history
                    f.write(f"[{route_tag}] {line_content}\n")
            typer.echo(f"Processing complete. Output written to '{output}'.")
        else:
            for (
                route_tag,
                line_content,
                trace_history,
            ) in result_iterator:  # Unpack trace_history
                trace_info = f" [Trace: {'>'.join(trace_history)}]" if trace else ""
                typer.echo(f"[{route_tag}] {line_content}{trace_info}")
            typer.echo("Processing complete. Output printed to console.")

    except Exception as e:
        typer.echo(f"An error occurred during processing or writing output: {e}")
        raise typer.Exit(code=1)

    if dashboard:
        typer.echo(
            "\nDashboard is still running. Press Ctrl+C to exit the application."
        )
        # Keep the main thread alive indefinitely if dashboard is running
        # Uvicorn runs indefinitely, so we need to ensure main thread doesn't exit
        # A simple input() or a loop can keep it alive.
        try:
            # This will block until Enter is pressed
            input("Press Enter to stop dashboard and exit application...\n")
        except KeyboardInterrupt:
            typer.echo("\nExiting gracefully.")
        finally:
            # In a real app, you'd have a more robust way to stop the dashboard thread.
            # For daemon threads, simply exiting the main thread will terminate them.
            pass


if __name__ == "__main__":
    app()
