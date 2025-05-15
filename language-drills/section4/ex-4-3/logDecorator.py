import functools

def log_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Executing {func.__name__} with arguments: {args} and keyword arguments: {kwargs}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} execution complete with result: {result}")
        return result
    return wrapper

# Example usage
@log_decorator
def add(a, b):
    """Adds two numbers."""
    return a + b

# Calling the decorated function
add(3, 5)

# Checking function name and docstring
print(f"Function name: {add.__name__}")
print(f"Function docstring: {add.__doc__}")
