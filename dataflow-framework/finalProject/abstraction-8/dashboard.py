# dashboard.py
import uvicorn
from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.responses import JSONResponse
from typing import (
    Dict,
    Any,
    List as PyList,
    Tuple,
    Optional,
    Annotated,
)  # Renamed List to PyList
import os
import shutil
from pathlib import Path
import logging

import observability_store  # Import the shared store

logger = logging.getLogger(__name__)

app = FastAPI(
    title="Processing Engine Dashboard",
    description="Live metrics, traces, file management for the data processing pipeline.",
)


# --- Health Check ---
@app.get("/health", summary="Health Check")
async def health_check():
    """Returns a simple health status."""
    return {"status": "healthy"}


# --- File Management Endpoints (for watch mode) ---
@app.get("/files", summary="List Processed and Unprocessed Files")
async def list_files() -> Dict[str, PyList[str]]:
    """
    Lists files currently in the configured 'unprocessed' and 'processed' directories.
    Only functional if the application is running in watch mode and `watch_dir` is configured.
    """
    watch_dir_config = getattr(app.state, "watch_dir_config", None)
    if not watch_dir_config:
        raise HTTPException(
            status_code=503,
            detail="File listing is not available. Watch mode may not be active or configured.",
        )

    unprocessed_dir = Path(watch_dir_config["unprocessed"])
    processed_dir = Path(watch_dir_config["processed"])

    response: Dict[str, PyList[str]] = {"unprocessed": [], "processed": []}

    try:
        if unprocessed_dir.exists() and unprocessed_dir.is_dir():
            response["unprocessed"] = [
                f.name for f in unprocessed_dir.iterdir() if f.is_file()
            ]
        else:
            logger.warning(
                f"/files endpoint: Unprocessed directory not found or not a directory: {unprocessed_dir}"
            )

        if processed_dir.exists() and processed_dir.is_dir():
            response["processed"] = [
                f.name for f in processed_dir.iterdir() if f.is_file()
            ]
        else:
            logger.warning(
                f"/files endpoint: Processed directory not found or not a directory: {processed_dir}"
            )

    except Exception as e:
        logger.error(f"Error listing files: {e}", exc_info=True)
        raise HTTPException(status_code=500, detail=f"Error listing files: {str(e)}")

    return response


@app.post("/upload/", summary="Upload File to Unprocessed Directory")
async def upload_file(file: UploadFile = File(...)) -> JSONResponse:
    """
    Uploads a file to the 'unprocessed' directory for processing in watch mode.
    """
    watch_dir_config = getattr(app.state, "watch_dir_config", None)
    if not watch_dir_config:
        raise HTTPException(
            status_code=503,
            detail="File upload is not available. Watch mode may not be active or configured.",
        )

    unprocessed_dir = Path(watch_dir_config["unprocessed"])

    if not unprocessed_dir.exists() or not unprocessed_dir.is_dir():
        logger.error(
            f"Upload target directory does not exist or is not a directory: {unprocessed_dir}"
        )
        raise HTTPException(
            status_code=500,
            detail=f"Upload directory '{unprocessed_dir.name}' not found on server.",
        )

    file_location = unprocessed_dir / file.filename

    # Basic security: prevent path traversal
    if ".." in file.filename or file.filename.startswith("/"):
        logger.warning(f"Potential path traversal attempt in filename: {file.filename}")
        raise HTTPException(status_code=400, detail="Invalid filename.")

    try:
        with open(file_location, "wb+") as file_object:
            shutil.copyfileobj(file.file, file_object)
        logger.info(
            f"File '{file.filename}' uploaded successfully to '{file_location}'."
        )
        return JSONResponse(
            status_code=201,
            content={
                "message": f"File '{file.filename}' uploaded successfully to '{unprocessed_dir.name}'. It will be processed shortly."
            },
        )
    except Exception as e:
        logger.error(
            f"Could not save uploaded file '{file.filename}': {e}", exc_info=True
        )
        raise HTTPException(status_code=500, detail=f"Could not save file: {str(e)}")
    finally:
        await file.close()


# --- Observability Endpoints ---
@app.get("/stats", summary="Live Processor Metrics")
async def get_stats() -> Dict[str, Dict[str, Any]]:
    """
    Returns live counts of lines received/emitted, processing times, and error counts
    for each processor.
    """
    return observability_store.get_all_metrics()


@app.get("/traces", summary="Recent Line Traces")
async def get_traces() -> PyList[Tuple[str, PyList[str]]]:  # Changed List to PyList
    """
    Returns a list of recent line traces, showing the path each line took through the system.
    Limited by the configured max size in the observability store (e.g., last 1000).
    """
    return observability_store.get_recent_traces()


@app.get("/errors", summary="Recent Processor Errors")
async def get_errors() -> PyList[
    Tuple[str, str, str, Optional[str]]
]:  # Changed List to PyList
    """
    Returns a list of recent errors that occurred within processors, including
    timestamp, processor name, error message, and the line content if available.
    Limited by the configured max size in the observability store (e.g., last 100).
    """
    return observability_store.get_recent_errors()


def start_dashboard_server():
    """Function to run the FastAPI server."""
    logger.info("Uvicorn server starting on http://0.0.0.0:8000")
    # Pass 'app' directly to uvicorn.run
    uvicorn.run(app, host="0.0.0.0", port=8000, log_level="info")


if __name__ == "__main__":
    # This allows running the dashboard standalone for testing, if needed.
    # However, it's typically started via cli.py.
    # Set up dummy state for standalone run if needed for /files or /upload
    if not hasattr(app.state, "watch_dir_config"):
        dummy_watch_dir = (
            Path(__file__).parent.parent / "watch_dir"
        )  # Adjust path as needed
        app.state.watch_dir_config = {
            "unprocessed": dummy_watch_dir / "unprocessed",
            "processed": dummy_watch_dir / "processed",
        }
        (dummy_watch_dir / "unprocessed").mkdir(parents=True, exist_ok=True)
        (dummy_watch_dir / "processed").mkdir(parents=True, exist_ok=True)
        logger.info(
            f"Running dashboard standalone with dummy watch_dir: {dummy_watch_dir}"
        )

    start_dashboard_server()
