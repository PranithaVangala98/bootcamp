import time


def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()  # Record the start time
        result = func(*args, **kwargs)  # Call the original function
        end_time = time.time()  # Record the end time
        execution_time = end_time - start_time  # Calculate the execution time
        print(f"Execution time of {func.__name__}: {execution_time:.6f} seconds")
        return result

    return wrapper


@timer
def slow_function():
    time.sleep(2)  # Simulate a slow function that takes 2 seconds


@timer
def fast_function():
    time.sleep(0.5)  # Simulate a function that takes 0.5 seconds


# Call the decorated functions
slow_function()
fast_function()
