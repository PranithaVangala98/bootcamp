import threading
import time


# Define a simple function to be run in the thread
def print_numbers():
    for i in range(5):
        print(i)
        time.sleep(1)


# Create a thread to run the print_numbers function
thread = threading.Thread(target=print_numbers)

# Start the thread
thread.start()

# Main program continues to run concurrently
for i in range(5, 10):
    print(i)
    time.sleep(1)

# Wait for the thread to finish before exiting the program
thread.join()

print("Thread has finished.")
