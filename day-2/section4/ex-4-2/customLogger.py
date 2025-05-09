def custom_logger(log_message):
    def decorator(func):
        def wrapper(*args, **kwargs):
            # Print the log message before function execution
            print(f"Before: {log_message}")

            # Execute the original function
            result = func(*args, **kwargs)

            # Print the log message after function execution
            print(f"After: {log_message}")
            return result

        return wrapper

    return decorator


@custom_logger("Executing greet function")
def greet(name):
    print(f"Hello, {name}!")


@custom_logger("Executing add function")
def add(a, b):
    return a + b


# Call the decorated functions
greet("Alice")
result = add(3, 4)
print("Addition result:", result)
