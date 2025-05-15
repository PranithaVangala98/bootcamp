# observability_store.py
import threading
import time
from collections import deque, defaultdict
from typing import Dict, Any, List, Tuple, Optional

# --- Metrics Store ---
# Structure: { "processor_name": { "received_count": int, "emitted_count": int, "processing_time_ms": float, "error_count": int } }
metrics: Dict[str, Dict[str, Any]] = defaultdict(
    lambda: {
        "received_count": 0,
        "emitted_count": 0,
        "processing_time_ms": 0.0,
        "error_count": 0,
    }
)
metrics_lock = threading.Lock()

# --- Traces Store ---
# Stores recent line traces (line_content, trace_history). Max size 1000.
traces: deque[Tuple[str, List[str]]] = deque(maxlen=1000)
traces_lock = threading.Lock()

# --- Errors Store ---
# Stores recent errors (timestamp, processor_name, error_message, line_content). Max size 100.
processor_errors: deque[Tuple[str, str, str, Optional[str]]] = deque(maxlen=100)
errors_lock = threading.Lock()


def initialize_metrics_for_processor(processor_name: str):
    """Ensures a processor's metrics entry exists."""
    with metrics_lock:
        # Accessing it via defaultdict will create it if it doesn't exist
        _ = metrics[processor_name]


def update_metrics_received(processor_name: str, count: int = 1):
    """Increments the received count for a processor."""
    with metrics_lock:
        metrics[processor_name]["received_count"] += count


def update_metrics_emitted(processor_name: str, count: int = 1):
    """Increments the emitted count for a processor."""
    with metrics_lock:
        metrics[processor_name]["emitted_count"] += count


def update_metrics_time(processor_name: str, duration_ms: float):
    """Adds processing time for a processor."""
    with metrics_lock:
        metrics[processor_name]["processing_time_ms"] += duration_ms


def update_metrics_error(processor_name: str, count: int = 1):
    """Increments the error count for a processor."""
    with metrics_lock:
        metrics[processor_name]["error_count"] += count


def add_trace(line_content: str, trace_history: List[str]):
    """Adds a line's journey trace."""
    with traces_lock:
        traces.append((line_content, trace_history))


def add_processor_error(
    processor_name: str, error_message: str, line_content: Optional[str] = None
):
    """Adds an error entry with timestamp."""
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
    with errors_lock:
        processor_errors.append(
            (timestamp, processor_name, error_message, line_content)
        )


def get_all_metrics() -> Dict[str, Dict[str, Any]]:
    """Returns a copy of all current metrics."""
    with metrics_lock:
        # Return a deep copy to prevent external modification
        return {k: v.copy() for k, v in metrics.items()}


def get_recent_traces() -> List[Tuple[str, List[str]]]:
    """Returns a list of recent traces."""
    with traces_lock:
        return list(traces)


def get_recent_errors() -> List[Tuple[str, str, str, Optional[str]]]:
    """Returns a list of recent errors."""
    with errors_lock:
        return list(processor_errors)


def reset_observability_store():
    """Resets all stored observability data."""
    with metrics_lock:
        metrics.clear()
    with traces_lock:
        traces.clear()
    with errors_lock:
        processor_errors.clear()
