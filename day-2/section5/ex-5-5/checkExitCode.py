import subprocess

# Run the command
result = subprocess.run(["ls", "-l"], capture_output=True, text=True)

# Check the exit code (returncode)
if result.returncode == 0:
    print("Command succeeded")
    print("Output:\n", result.stdout)
else:
    print(f"Command failed with exit code {result.returncode}")
    print("Error:\n", result.stderr)
