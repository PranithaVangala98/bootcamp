class MyContext:
    def __enter__(self):
        print("Entering context")
        return self  # Optional, return value is assigned to `as` variable if used

    def __exit__(self, exc_type, exc_value, traceback):
        print("Exiting context")
        if exc_type:
            print(f"An exception occurred: {exc_value}")
        # Return False to propagate exception, True to suppress
        return False

# Using the custom context manager
with MyContext():
    print("Inside the context block")
