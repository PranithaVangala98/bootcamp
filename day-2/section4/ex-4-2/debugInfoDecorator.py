def debug_info(func):
    def wrapper(*args, **kwargs):
        # Print function name and arguments
        print(f"Calling function: {func.__name__}")
        print(f"Arguments: {args}, Keyword arguments: {kwargs}")

        # Call the actual function
        result = func(*args, **kwargs)

        # Print the return value
        print(f"Return value: {result}")
        return result

    return wrapper


@debug_info
def add(a, b):
    return a + b


@debug_info
def greet(name, age):
    return f"Hello {name}, you are {age} years old."


# Call the decorated functions
add(5, 3)
greet("Alice", 30)
