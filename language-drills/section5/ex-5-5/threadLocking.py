import threading

# Shared variable
shared_counter = 0

# Create a Lock object
lock = threading.Lock()


# Define a function to increment the shared counter
def increment_counter():
    global shared_counter
    # Acquire the lock before modifying the shared resource
    with lock:
        for _ in range(100000):
            shared_counter += 1
    # Lock is automatically released when the block is exited


# Create multiple threads that will modify the shared counter
threads = []
for _ in range(5):
    thread = threading.Thread(target=increment_counter)
    threads.append(thread)
    thread.start()

# Wait for all threads to finish
for thread in threads:
    thread.join()

# Print the final value of the shared counter
print("Final counter value:", shared_counter)
