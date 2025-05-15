from pathlib import Path

# Define a relative path
relative_path = Path("example.txt")

# Get the absolute path
absolute_path = relative_path.resolve()

print(f"Relative path: {relative_path}")
print(f"Absolute path: {absolute_path}")
