# Data Processing Pipeline with Real-time Observability
This project implements a flexible, tag-based state transition engine for processing data lines, enhanced with real-time observability features via a web dashboard. It's designed to handle complex data flows found in data pipelines, workflow automation, and event processing systems, providing crucial operational insights.

## 🌟 Features
### Core Processing Engine
Dynamic Tag-based Routing: Lines flow through the system based on dynamically assigned tags. Each processor consumes lines tagged with a specific name and emits lines with new tags, determining the next processing step.
#### State Machine Behavior: 
Processors act as "states," and tag-based emissions represent "transitions" between these states.
Fan-out & Fan-in: Supports a processor emitting lines with multiple different tags (fan-out) and a single processor receiving lines from multiple input tags (fan-in).
#### Cyclic Flows: 
The system does not assume acyclicity, allowing for complex looping flows (e.g., retries, feedback loops).
Modular Processors: Processing logic is encapsulated in independent Python functions/callables, making the pipeline highly extensible and configurable via a YAML file (pipeline.yaml).
Real-time Observability & Web Dashboard
#### Live Metrics: 
Track key performance indicators for each processor in real-time:
#### Lines Received: 
Count of lines entering the processor.
#### Lines Emitted: 
Count of lines produced by the processor.
#### Processing Time:
 Total time spent by the processor on its tasks (in milliseconds).
#### Error Count:
 Number of exceptions encountered by the processor.
#### Execution Tracing:
 Optionally record the complete journey (sequence of tags/processors) for individual lines as they traverse the pipeline. This provides a granular view of data flow and transformation.
#### Error Logging: 
Store recent exceptions encountered by processors, including details like timestamp, processor name, the error message, and the problematic line content (if available).
#### Web Dashboard (FastAPI):
 A lightweight web interface runs on a separate thread, providing live endpoints for:
/stats: Current aggregate processor metrics.
/traces: Recent line execution traces.
/errors: Recent processor-level error logs.
#### Concurrency: 
The web dashboard operates concurrently with the main data processing pipeline, ensuring minimal impact on performance. Shared data structures are protected by threading.Lock for thread safety.
### 🚀 Real-World Motivation
In production environments, understanding the health, performance, and behavior of data processing systems is paramount. This project addresses common operational needs:

#### Debugging & Troubleshooting: 
Trace the path of a specific problematic record to pinpoint where issues occur. Instantly see error details without sifting through logs.
#### Performance Monitoring: 
Identify slow or overloaded processors to optimize resource allocation or code.
#### Operational Transparency:
 Get a live overview of data throughput and processing stages, allowing for proactive monitoring and anomaly detection.
#### System Health:
 Monitor error rates and processing times to ensure the pipeline is operating within expected parameters.
### 🏗️ System Architecture
The system is modular and consists of the following key components:

- main.py: The main entry point of the application.
cli.py: Handles command-line arguments (input/output files, enabling dashboard/tracing) and orchestrates the start of the processing and dashboard threads.
- pipeline.yaml: The declarative configuration file defining the processing graph by mapping route tags to Python processor functions.
- pipeline.py: Responsible for loading and parsing pipeline.yaml and dynamically resolving the Python processor functions.
- core.py: The heart of the state transition engine. It manages the queues of TaggedLines, dispatches them to appropriate processors based on their current tag, instruments processor calls to capture metrics and traces, handles exceptions, and updates the shared observability store.
- processors/: A directory containing individual Python modules. Each module defines one or more ProcessorFns – functions that transform input lines and yield output lines with new tags.
- types1.py: Defines core data structures like Route, ProcessorFn, Trace, and the crucial TaggedLine (which now includes trace history).
- core_utils.py: Provides utility decorators (@linewise, @tag_aware_linewise) to simplify the creation of new processor functions.
- observability_store.py: A dedicated module housing thread-safe global data structures (dictionaries and deques protected by threading.Lock) for storing live metrics, recent traces, and recent errors. It provides controlled access functions to these stores.
- dashboard.py: Implements the FastAPI web server, defining the API endpoints (/stats, /traces, /errors) that query the observability_store and serve the data as JSON.
- The core.py module is central to the observability aspect; it transparently wraps processor calls, measuring execution time, updating line counts, capturing exceptions, and appending to the trace history of each line as it moves between processors.

## 🏁 Getting Started
### Prerequisites
- Python 3.8+
- pip (Python package installer)
- Installation
- Clone the repository or ensure your project structure matches the provided code.
#### Install the required Python packages:
- Bash

- pip install typer pyyaml python-dotenv "fastapi[all]" uvicorn
Running the Application

### Prepare Input Data
Create an input.txt file in your project root with some sample lines. This input is designed to demonstrate all features, especially if you apply the temporary error simulation (see below).

#### input.txt content:

This is a normal log entry.

WARNING: Low disk space alert.

Another general log line.

ERROR: Database connection failed.

Processing important data now.

This line will intentionally cause an error if modified.

Warning: unusual activity detected.

This is the final line of the input.

#### Run from the Command Line

Execute the following command from your project's root directory:

Bash

```
uv run main.py --input input.txt --dashboard --trace
--input input.txt: Specifies the input file for processing.
```
- --dashboard: Starts the FastAPI web dashboard, accessible via http://localhost:8000/.

- --trace: Enables execution tracing, allowing you to see the full path of each line in the console output and on the /traces dashboard endpoint.
#### Observe Console Output
The terminal will display the processed lines with their final tags. If --trace is enabled, you'll also see the full trace history for each line.

Example of console output:

Starting web dashboard at http://localhost/:8000/...
[formatted_general] INFO: This is a normal log entry. [Trace: 

input>needs_classification>general>formatted_general]
[tallied_warning] Tallied Warning #1: Warning: Low disk space alert. [Trace: input>needs_classification>warnings>tallied_warning]
...

[general_failed] This line will intentionally cause an error if modified. [Trace: input>needs_classification>general>general_failed]
...

Processing complete. Output printed to console.

Dashboard is still running. Press Ctrl+C to exit the application.
Press Enter to stop dashboard and exit application...

Check the Web Dashboard
While the application is running (before pressing Enter in the console):

http://localhost:8000/stats: View real-time metrics for all processors (lines received, emitted, processing time, error count).
http://localhost:8000/traces: See the execution traces for the most recently processed lines. Each entry will show the original line content and the sequence of tags it passed through.
http://localhost:8000/errors: View recent errors that occurred within processors, including timestamps, processor names, error messages, and the problematic line content.

