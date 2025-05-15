from pathlib import Path

# Define a path
path = Path("example.txt")

# Check if the path exists
if path.exists():
    print(f"Path '{path}' exists.")
    
    # Check if the path is a file
    if path.is_file():
        print(f"'{path}' is a file.")
    else:
        print(f"'{path}' is not a file.")
else:
    print(f"Path '{path}' does not exist.")
