import subprocess

# Run the command and capture its output
result = subprocess.run(["ls", "-l"], capture_output=True, text=True)

# Store the output and error (if any)
output = result.stdout
error = result.stderr

# Print the captured output and error
print("Captured Output:\n", output)
if error:
    print("Captured Error:\n", error)
