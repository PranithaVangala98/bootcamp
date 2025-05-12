# Makefile

# Default Python interpreter
PYTHON = python3

# Default watch directory
WATCH_DIR ?= ./watch_dir
UNPROCESSED_DIR = $(WATCH_DIR)/unprocessed
PROCESSED_DIR = $(WATCH_DIR)/processed

# Docker image name
DOCKER_IMAGE_NAME = file-processor-system
DOCKER_CONTAINER_NAME = file-processor-app

.PHONY: help run run-file run-watch build-docker run-docker stop-docker logs-docker clean test build-package publish-package format lint setup

help:
	@echo "Makefile for the Real-Time File Processing System"
	@echo ""
	@echo "Usage:"
	@echo "  make setup             Install dependencies and create watch directories"
	@echo "  make run-file          Run in single file mode. Args: INPUT_FILE, [OUTPUT_FILE, CONFIG, DASHBOARD, TRACE, DEBUG]"
	@echo "                         Example: make run-file INPUT_FILE=test.txt DASHBOARD=true"
	@echo "  make run-watch         Run in watch mode. Args: [WATCH_DIR, CONFIG, DASHBOARD, TRACE, DEBUG]"
	@echo "                         Example: make run-watch DASHBOARD=true"
	@echo "  make build-docker      Build the Docker image"
	@echo "  make run-docker        Run the application in a Docker container (watch mode)"
	@echo "  make stop-docker       Stop the running Docker container"
	@echo "  make logs-docker       View logs from the Docker container"
	@echo "  make clean             Remove Python cache files and processed files"
	@echo "  make test              Run tests (placeholder)"
	@echo "  make format            Format code using Black and isort"
	@echo "  make lint              Lint code using Flake8"
	@echo "  make build-package     Build a distributable package (placeholder)"
	@echo "  make publish-package   Publish the package (placeholder)"
	@echo ""
	@echo "Argument examples for run commands:"
	@echo "  INPUT_FILE: path to the input file (for run-file)"
	@echo "  OUTPUT_FILE: path to the output file (optional, for run-file)"
	@echo "  WATCH_DIR: root directory for watching (for run-watch, default: ./watch_dir)"
	@echo "  CONFIG: path to pipeline.yaml (optional, default: pipeline.yaml)"
	@echo "  DASHBOARD: true/false to run dashboard (optional, default: false)"
	@echo "  TRACE: true/false to enable tracing (optional, default: false)"
	@echo "  DEBUG: true/false to enable debug logging (optional, default: false)"

setup:
	@echo "Installing dependencies..."
	$(PYTHON) -m pip install -r requirements.txt
	@echo "Creating watch directories if they don't exist..."
	mkdir -p $(UNPROCESSED_DIR)
	mkdir -p $(PROCESSED_DIR)
	@echo "Setup complete. Ensure your processor modules are in the 'processors' directory."

# --- CLI Arguments ---
# These allow passing arguments like `make run-file INPUT_FILE=myfile.txt`
INPUT_FILE_ARG = $(if $(INPUT_FILE),--input $(INPUT_FILE),)
OUTPUT_FILE_ARG = $(if $(OUTPUT_FILE),--output $(OUTPUT_FILE),)
WATCH_DIR_ARG = $(if $(WATCH_DIR_CMD),--watch-dir $(WATCH_DIR_CMD),--watch-dir $(WATCH_DIR)) # WATCH_DIR_CMD for explicit override
CONFIG_ARG = $(if $(CONFIG),--config $(CONFIG),)
DASHBOARD_ARG = $(if $(DASHBOARD),--dashboard,)
TRACE_ARG = $(if $(TRACE),--trace,)
DEBUG_ARG = $(if $(DEBUG),--debug,)

CLI_ARGS = $(CONFIG_ARG) $(DASHBOARD_ARG) $(TRACE_ARG) $(DEBUG_ARG)

run-file:
ifndef INPUT_FILE
	$(error INPUT_FILE is not set. Usage: make run-file INPUT_FILE=path/to/file.txt)
endif
	@echo "Running in single file mode for: $(INPUT_FILE)"
	$(PYTHON) main.py $(INPUT_FILE_ARG) $(OUTPUT_FILE_ARG) $(CLI_ARGS)

run-watch:
	@echo "Running in watch mode, monitoring: $(WATCH_DIR_ARG)"
	$(PYTHON) main.py --watch $(WATCH_DIR_ARG) $(CLI_ARGS)

# --- Docker Operations ---
build-docker:
	@echo "Building Docker image: $(DOCKER_IMAGE_NAME)..."
	docker build -t $(DOCKER_IMAGE_NAME) .

run-docker:
	@echo "Running $(DOCKER_IMAGE_NAME) in a container named $(DOCKER_CONTAINER_NAME)..."
	@echo "Dashboard will be available at http://localhost:8000"
	@echo "Watching directory: $(WATCH_DIR) (mounted to /app/watch_dir in container)"
	docker run -d -p 8000:8000 \
		-v "$(CURDIR)/watch_dir":/app/watch_dir \
		-v "$(CURDIR)/pipeline.yaml":/app/pipeline.yaml \
		-v "$(CURDIR)/processors":/app/processors \
		--name $(DOCKER_CONTAINER_NAME) $(DOCKER_IMAGE_NAME)

stop-docker:
	@echo "Stopping Docker container: $(DOCKER_CONTAINER_NAME)..."
	docker stop $(DOCKER_CONTAINER_NAME) || echo "Container not running or already stopped."
	@echo "Removing Docker container: $(DOCKER_CONTAINER_NAME)..."
	docker rm $(DOCKER_CONTAINER_NAME) || echo "Container not found or already removed."

logs-docker:
	@echo "Showing logs for Docker container: $(DOCKER_CONTAINER_NAME)..."
	docker logs -f $(DOCKER_CONTAINER_NAME)

# --- Utility ---
clean:
	@echo "Cleaning up..."
	find . -type f -name '*.py[co]' -delete
	find . -type d -name '__pycache__' -delete
	rm -f $(PROCESSED_DIR)/*
	@echo "Cleaned."

test:
	@echo "Running tests... (placeholder)"
	# Add your test commands here, e.g., pytest

# --- Packaging (Placeholders) ---
build-package:
	@echo "Building package... (placeholder)"
	# $(PYTHON) setup.py sdist bdist_wheel

publish-package:
	@echo "Publishing package... (placeholder)"
	# twine upload dist/*

# --- Code Quality ---
format:
	@echo "Formatting code with Black and isort..."
	$(PYTHON) -m black .
	$(PYTHON) -m isort .

lint:
	@echo "Linting code with Flake8..."
	$(PYTHON) -m flake8 .
