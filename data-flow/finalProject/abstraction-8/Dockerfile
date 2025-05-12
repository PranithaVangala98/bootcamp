# Dockerfile
# Use an official Python runtime as a parent image
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container at /app
COPY requirements.txt .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container at /app
# Ensure .dockerignore is set up to exclude venv, .git, etc.
COPY . .

# Make port 8000 available to the world outside this container (for FastAPI dashboard)
EXPOSE 8000

# Define environment variables (if any)
# ENV NAME World

# Create necessary directories for watch mode within the container
RUN mkdir -p /app/watch_dir/unprocessed /app/watch_dir/processed

# Command to run the application
# By default, runs in watch mode with the dashboard.
# Assumes main.py is the entry point and cli.py handles arguments.
CMD ["python", "main.py", "--watch", "--dashboard", "--watch-dir", "/app/watch_dir"]
