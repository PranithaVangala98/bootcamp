class DatabaseConnection:
    def __enter__(self):
        print("Opening database connection...")
        # Simulate acquiring a DB resource
        self.connection = "DB_CONNECTION_OBJECT"
        return self.connection

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Closing database connection...")
        # Simulate releasing the DB resource
        self.connection = None
        if exc_type:
            print(f"An error occurred: {exc_val}")
        # Do not suppress exceptions
        return False

# Use the simulated database connection
with DatabaseConnection() as conn:
    print(f"Using {conn} to perform queries")
    # Uncomment to simulate an error
    # raise Exception("Simulated DB error")
