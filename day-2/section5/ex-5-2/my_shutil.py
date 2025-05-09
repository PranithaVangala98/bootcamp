import shutil
from pathlib import Path

# Define the source and destination paths
source = Path("source_file.txt")
destination = Path("destination_file.txt")

# Copy the file from source to destination
shutil.copy(source, destination)

print(f"File copied from {source} to {destination}")
