class Resource:
    def __enter__(self):
        print("Resource acquired.")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Resource released.")
        if exc_type:
            print(f"Handled error: {exc_val}")
        # Return False to propagate the exception
        return False

# Use the context manager
try:
    with Resource() as res:
        print("Using the resource.")
        raise ValueError("Something went wrong!")  # Simulate an error
except Exception as e:
    print(f"Caught exception: {e}")
