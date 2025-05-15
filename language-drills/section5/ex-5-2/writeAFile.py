from pathlib import Path

# Specify the file path
file_path = Path("example.txt")

# Write "hello" to the file
file_path.write_text("hello")

print("Text written to file")

# Open the file in write mode
with open("example.txt", "w") as file:
    # Write "hello" to the file
    file.write("hello")

print("Text written to file")
