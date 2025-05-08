import time


# Simple logger decorator
def simple_logger(func):
    def wrapper(*args, **kwargs):
        print("Function started")
        result = func(*args, **kwargs)
        print("Function ended")
        return result

    return wrapper


# Timer decorator
def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Execution time: {end_time - start_time:.6f} seconds")
        return result

    return wrapper


# Debug info decorator
def debug_info(func):
    def wrapper(*args, **kwargs):
        print(f"Calling function: {func.__name__}")
        print(f"Arguments: {args}, Keyword arguments: {kwargs}")
        result = func(*args, **kwargs)
        print(f"Return value: {result}")
        return result

    return wrapper


@simple_logger
@timer
@debug_info
def sample_function(x, y):
    return x + y


sample_function(3, 4)
