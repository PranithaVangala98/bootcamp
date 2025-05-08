from pathlib import Path

# Specify the file path
file_path = Path("myfile.txt")

# Read the file content
content = file_path.read_text()

# Print the content
print(content)
