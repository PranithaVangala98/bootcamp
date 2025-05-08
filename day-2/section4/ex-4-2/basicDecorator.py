def simple_logger(func):
    def wrapper(*args, **kwargs):
        print("Function started")
        result = func(*args, **kwargs)
        print("Function ended")
        return result

    return wrapper


@simple_logger
def greet(name):
    print(f"Hello, {name}!")


# Call the decorated function
greet("Pranitha")
