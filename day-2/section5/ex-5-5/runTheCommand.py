import subprocess
import platform

# Determine the operating system
if platform.system() == "Windows":
    # Windows equivalent command
    command = ["dir"]
else:
    # Unix-based (Linux/macOS) command
    command = ["ls", "-l"]

# Run the command
result = subprocess.run(command, capture_output=True, text=True)

# Print the output of the command
print(result.stdout)
