import os
import shutil
from pathlib import Path

# Create a temporary directory
temp_dir = Path("temp_dir")
os.makedirs(temp_dir, exist_ok=True)

# Create a file inside the temporary directory
temp_file = temp_dir / "example.txt"
with open(temp_file, "w") as f:
    f.write("This is a temporary file.")

# Verify the file and directory are created
print(f"File created: {temp_file.exists()}")

# Safely remove the directory and its contents
shutil.rmtree(temp_dir)

# Verify the directory and file are deleted
print(f"Directory exists after deletion: {temp_dir.exists()}")
    