def prefix_printer(prefix):
    def decorator(func):
        def wrapper(*args, **kwargs):
            print(f"{prefix} {func.__name__}")
            return func(*args, **kwargs)

        return wrapper

    return decorator


@prefix_printer("Calling function:")
def greet(name):
    print(f"Hello, {name}!")


@prefix_printer("Function call:")
def add(a, b):
    return a + b


# Call the decorated functions
greet("Alice")
result = add(3, 4)
print("Result of addition:", result)
