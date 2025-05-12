# cli.py
import typer
from typing import Optional, Iterator, List as PyList
import threading
import time
import os
import shutil
import logging  # For logging
from pathlib import Path

from dotenv import load_dotenv
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from pipeline import get_processors
from core import process_lines
from types1 import TaggedLine, Route
import observability_store
from dashboard import (
    start_dashboard_server,
    app as fastapi_app,
)  # Import FastAPI app for health/files

load_dotenv()
logger = logging.getLogger(__name__)  # Get logger instance

app = typer.Typer(help="Real-Time File Processing System CLI")

INITIAL_ROUTE_TAG: Route = "input"
DEFAULT_WATCH_DIR = Path("./watch_dir")  # Default watch directory


# --- Helper function to process a single file ---
def _process_single_file(
    filepath: Path,
    output_filepath: Optional[Path],
    processors_map: dict,
    initial_route_tag: Route,
    trace_enabled: bool,
    dashboard_running: bool,
):
    """
    Processes a single file and handles output.
    """
    logger.info(f"Processing file: {filepath}")
    try:
        with open(filepath, "r") as f_in:
            lines_content = [line.rstrip("\n") for line in f_in]
    except FileNotFoundError:
        logger.error(f"Input file not found: {filepath}")
        typer.echo(f"Error: Input file '{filepath}' not found.", err=True)
        return False  # Indicate failure
    except Exception as e:
        logger.error(f"Error reading input file '{filepath}': {e}")
        typer.echo(f"Error reading input file '{filepath}': {e}", err=True)
        return False

    result_iterator: Iterator[TaggedLine] = process_lines(
        iter(lines_content),
        processors_map,
        initial_route_tag,
        trace_enabled=trace_enabled,
    )

    output_lines: PyList[str] = []
    try:
        for route_tag, line_content, trace_history in result_iterator:
            trace_info = (
                f" [Trace: {'>'.join(trace_history)}]"
                if trace_enabled and trace_history
                else ""
            )
            formatted_line = f"[{route_tag}] {line_content}{trace_info}"
            if not output_filepath:  # Print to console if no output file
                if (
                    not dashboard_running
                ):  # Avoid duplicate console output if dashboard also logs
                    typer.echo(formatted_line)
            output_lines.append(formatted_line)

        if output_filepath:
            with open(output_filepath, "w") as f_out:
                for line in output_lines:
                    f_out.write(line + "\n")
            logger.info(f"Output written to {output_filepath}")
            if not dashboard_running:
                typer.echo(
                    f"Processing complete. Output written to '{output_filepath}'."
                )
        elif (
            not dashboard_running
        ):  # Only print this if not in dashboard mode (dashboard has its own logs)
            typer.echo("Processing complete. Output printed to console.")
        return True  # Indicate success

    except Exception as e:
        logger.error(f"Error during processing or writing output for {filepath}: {e}")
        typer.echo(
            f"An error occurred during processing or writing output for {filepath}: {e}",
            err=True,
        )
        return False


# --- Watchdog Event Handler ---
class WatcherEventHandler(FileSystemEventHandler):
    def __init__(
        self,
        processors_map: dict,
        initial_route_tag: Route,
        trace_enabled: bool,
        output_dir: Path,  # Where to move processed files
        unprocessed_dir: Path,  # To confirm the event is in the right place
        dashboard_running: bool,
    ):
        self.processors_map = processors_map
        self.initial_route_tag = initial_route_tag
        self.trace_enabled = trace_enabled
        self.output_dir = output_dir
        self.unprocessed_dir = unprocessed_dir
        self.dashboard_running = dashboard_running
        logger.info(
            f"File watcher initialized. Monitoring: {self.unprocessed_dir}, Processed files to: {self.output_dir}"
        )

    def on_created(self, event):
        if event.is_directory:
            return

        src_path = Path(event.src_path)
        # Ensure the file is directly in the unprocessed_dir (not a subdirectory)
        if src_path.parent != self.unprocessed_dir:
            logger.debug(f"Ignoring file created outside unprocessed_dir: {src_path}")
            return

        # Add a small delay to ensure file is fully written
        time.sleep(0.5)
        logger.info(f"New file detected: {src_path}")

        # Define a unique output file name in the processed directory to avoid clashes
        # (though moving should handle this, this is good practice if copying)
        # timestamp = time.strftime("%Y%m%d-%H%M%S")
        # output_filename = f"{src_path.stem}_{timestamp}{src_path.suffix}"
        # For simplicity, we'll just move with the same name.
        # Ensure the output directory exists
        self.output_dir.mkdir(parents=True, exist_ok=True)

        # No separate output file for watched files; they are processed and then moved.
        # The _process_single_file function will print to console if dashboard isn't running.
        success = _process_single_file(
            filepath=src_path,
            output_filepath=None,  # Output is handled by moving the file
            processors_map=self.processors_map,
            initial_route_tag=self.initial_route_tag,
            trace_enabled=self.trace_enabled,
            dashboard_running=self.dashboard_running,
        )

        if success:
            try:
                destination_path = self.output_dir / src_path.name
                shutil.move(str(src_path), str(destination_path))
                logger.info(
                    f"Successfully processed and moved '{src_path.name}' to '{destination_path}'"
                )
            except Exception as e:
                logger.error(
                    f"Failed to move processed file '{src_path.name}' to '{self.output_dir}': {e}"
                )
        else:
            logger.warning(
                f"File '{src_path.name}' was not processed successfully. It will remain in '{self.unprocessed_dir}'."
            )
            # Optionally, move to an error directory:
            # error_dir = self.unprocessed_dir.parent / "failed"
            # error_dir.mkdir(parents=True, exist_ok=True)
            # shutil.move(str(src_path), str(error_dir / src_path.name))
            # logger.info(f"Moved '{src_path.name}' to error directory: {error_dir}")


# --- Main CLI Command ---
@app.command()
def run(
    input_file: Optional[Path] = typer.Option(
        None,
        "--input",
        "-i",
        help="Path to a single input file to process.",
        exists=True,
        file_okay=True,
        dir_okay=False,
        readable=True,
        resolve_path=True,
    ),
    watch: bool = typer.Option(
        False,
        "--watch",
        "-w",
        help="Enable watch mode to monitor a directory for new files.",
    ),
    watch_dir: Path = typer.Option(
        DEFAULT_WATCH_DIR,
        "--watch-dir",
        help="Directory to watch for files (root for unprocessed/processed).",
        exists=True,
        file_okay=False,
        dir_okay=True,
        readable=True,
        resolve_path=True,
    ),
    output_file: Optional[Path] = typer.Option(
        None,
        "--output",
        "-o",
        help="Output filename (only for single file mode).",
        file_okay=True,
        dir_okay=False,
        writable=True,
        resolve_path=True,
    ),
    config: Path = typer.Option(
        "pipeline.yaml",
        "--config",
        "-c",
        help="Path to YAML config file.",
        exists=True,
        file_okay=True,
        dir_okay=False,
        readable=True,
        resolve_path=True,
    ),
    dashboard: bool = typer.Option(
        False,
        "--dashboard",
        "-d",
        help="Run the web dashboard for live metrics and traces.",
    ),
    trace: bool = typer.Option(
        False, "--trace", "-t", help="Enable execution tracing for lines."
    ),
    debug: bool = typer.Option(False, "--debug", help="Enable debug logging."),
):
    """
    Processes files using a configurable pipeline.
    Run in single file mode (--input) or watch mode (--watch).
    """
    if debug:
        logging.getLogger().setLevel(logging.DEBUG)
        logger.debug("Debug logging enabled.")
    else:
        logging.getLogger().setLevel(logging.INFO)  # Ensure it's INFO if not debug

    if not input_file and not watch:
        typer.echo(
            "Error: Please specify either --input for single file mode or --watch for watch mode.",
            err=True,
        )
        raise typer.Exit(code=1)
    if input_file and watch:
        typer.echo(
            "Error: --input and --watch options are mutually exclusive.", err=True
        )
        raise typer.Exit(code=1)
    if output_file and watch:
        typer.echo(
            "Warning: --output is ignored in --watch mode. Processed files are moved.",
            err=False,
        )  # Not an error, just a warning

    # Reset observability store for a clean run
    observability_store.reset_observability_store()
    logger.info("Observability store reset.")

    # --- Load Pipeline Configuration ---
    try:
        processors_map, _routing_config = get_processors(str(config))
        logger.info(
            f"Pipeline configuration loaded successfully from '{config}'. {len(processors_map)} processors found."
        )
    except FileNotFoundError:
        logger.error(f"Config file not found: {config}")
        typer.echo(f"Error: Config file '{config}' not found.", err=True)
        raise typer.Exit(code=1)
    except (ValueError, ImportError) as e:
        logger.error(f"Error loading pipeline configuration: {e}")
        typer.echo(f"Error loading pipeline configuration or processors: {e}", err=True)
        raise typer.Exit(code=1)

    # --- Start Dashboard if enabled ---
    dashboard_thread: Optional[threading.Thread] = None
    if dashboard:
        logger.info("Starting web dashboard...")
        typer.echo("Starting web dashboard at http://0.0.0.0:8000...")
        # Pass watch_dir to dashboard for /files endpoint
        fastapi_app.state.watch_dir_config = {
            "unprocessed": watch_dir / "unprocessed",
            "processed": watch_dir / "processed",
        }
        fastapi_app.state.pipeline_config_path = (
            config  # For potential future use by dashboard
        )

        dashboard_thread = threading.Thread(target=start_dashboard_server, daemon=True)
        dashboard_thread.start()
        time.sleep(1.5)  # Give server a moment to start
        if dashboard_thread.is_alive():
            logger.info("Web dashboard started successfully.")
        else:
            logger.error("Web dashboard failed to start.")
            typer.echo("Error: Web dashboard failed to start.", err=True)
            # Optionally exit if dashboard is critical, or just continue
            # raise typer.Exit(code=1)

    # --- Execute Mode ---
    try:
        if input_file:
            logger.info(f"Running in single file mode for: {input_file}")
            _process_single_file(
                input_file,
                output_file,
                processors_map,
                INITIAL_ROUTE_TAG,
                trace,
                dashboard,
            )
            if dashboard:
                typer.echo(
                    "Single file processing complete. Dashboard is still running."
                )
                typer.echo("Press Ctrl+C to stop the dashboard and exit.")
                try:
                    while True:
                        time.sleep(1)  # Keep alive for dashboard
                except KeyboardInterrupt:
                    logger.info("Dashboard shutdown requested via Ctrl+C.")

        elif watch:
            unprocessed_dir = watch_dir / "unprocessed"
            processed_dir = watch_dir / "processed"
            unprocessed_dir.mkdir(parents=True, exist_ok=True)
            processed_dir.mkdir(parents=True, exist_ok=True)

            logger.info(
                f"Running in watch mode. Monitoring directory: {unprocessed_dir}"
            )
            typer.echo(f"Watch mode enabled. Monitoring: {unprocessed_dir}")
            typer.echo(f"Processed files will be moved to: {processed_dir}")
            if not dashboard:
                typer.echo("Press Ctrl+C to stop watching and exit.")

            event_handler = WatcherEventHandler(
                processors_map,
                INITIAL_ROUTE_TAG,
                trace,
                processed_dir,
                unprocessed_dir,
                dashboard,
            )
            observer = Observer()
            observer.schedule(
                event_handler, str(unprocessed_dir), recursive=False
            )  # Only watch top-level
            observer.start()
            logger.info("File observer started.")

            try:
                while True:
                    time.sleep(1)
            except KeyboardInterrupt:
                logger.info("Watch mode interrupted by user (Ctrl+C). Shutting down...")
                typer.echo("\nStopping watcher...")
            finally:
                observer.stop()
                observer.join()
                logger.info("File observer stopped.")

    except Exception as e:
        logger.critical(
            f"An unhandled error occurred in run command: {e}", exc_info=True
        )
        typer.echo(f"An critical error occurred: {e}", err=True)
        raise typer.Exit(code=1)
    finally:
        if dashboard and dashboard_thread and dashboard_thread.is_alive():
            # Uvicorn in a daemon thread will be stopped when the main thread exits.
            # No explicit stop needed unless you implement a graceful shutdown for Uvicorn.
            logger.info(
                "Application exiting. Dashboard (if running as daemon) will also terminate."
            )
        typer.echo("Application finished.")


if __name__ == "__main__":
    # This is important for Typer to work correctly when script is run directly
    # and also allows main.py to call app()
    app()
