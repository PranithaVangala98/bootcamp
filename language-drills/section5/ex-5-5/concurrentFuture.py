import concurrent.futures
import time


# Define a function that we want to execute concurrently
def compute_square(number):
    time.sleep(1)  # Simulate a time-consuming task
    return number * number


# List of numbers to compute squares for
numbers = [1, 2, 3, 4, 5]

# Using ThreadPoolExecutor to parallelize the computation
with concurrent.futures.ThreadPoolExecutor() as executor:
    # Map the function to the numbers (equivalent to calling compute_square for each number in parallel)
    results = list(executor.map(compute_square, numbers))

# Print the results
print("Results:", results)
