# dashboard.py
import uvicorn
from fastapi import FastAPI
from typing import Dict, Any, List, Tuple, Optional

import observability_store  # Import the shared store

app = FastAPI(
    title="Processing Engine Dashboard",
    description="Live metrics and traces for the data processing pipeline.",
)


@app.get("/stats", summary="Live Processor Metrics")
async def get_stats() -> Dict[str, Dict[str, Any]]:
    """
    Returns live counts of lines received/emitted, processing times, and error counts
    for each processor.
    """
    return observability_store.get_all_metrics()


@app.get("/traces", summary="Recent Line Traces")
async def get_traces() -> List[Tuple[str, List[str]]]:
    """
    Returns a list of recent line traces, showing the path each line took through the system.
    Limited by the configured max size in the observability store (e.g., last 1000).
    """
    return observability_store.get_recent_traces()


@app.get("/errors", summary="Recent Processor Errors")
async def get_errors() -> List[Tuple[str, str, str, Optional[str]]]:
    """
    Returns a list of recent errors that occurred within processors, including
    timestamp, processor name, error message, and the line content if available.
    Limited by the configured max size in the observability store (e.g., last 100).
    """
    return observability_store.get_recent_errors()


def start_dashboard_server():
    """Function to run the FastAPI server."""
    # Use reload=False for production-like environments, but good for dev
    uvicorn.run(app, host="0.0.0.0", port=8000, log_level="warning")
