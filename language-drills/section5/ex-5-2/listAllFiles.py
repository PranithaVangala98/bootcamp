from pathlib import Path

# List all Python files in the current directory
python_files = Path(".").glob("*.py")

# Print each Python file
for file in python_files:
    print(file)
