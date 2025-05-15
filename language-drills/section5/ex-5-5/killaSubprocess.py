import subprocess
import time

# Start a long-running subprocess (e.g., a command that sleeps for a long time)
process = subprocess.Popen(["sleep", "10"])

# Wait for a certain amount of time (e.g., 3 seconds)
time.sleep(3)

# Terminate the subprocess
process.terminate()

# Check if the process is still alive
if process.poll() is None:
    print("The process is still running, now terminating it.")
else:
    print("The process has already finished.")

# Wait for the process to fully terminate
process.wait()

print("Subprocess terminated.")
