from functools import wraps

def my_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with arguments {args} and keyword arguments {kwargs}")
        return func(*args, **kwargs)
    return wrapper


@my_decorator
def greet(name):
    """Greets a person by their name."""
    return f"Hello, {name}!"

print(greet("Alice"))


print(f"Function name: {greet.__name__}")
print(f"Function docstring: {greet.__doc__}")
