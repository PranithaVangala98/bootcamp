class Greeter:
    def __init__(self, greeting):
        self.greeting = greeting

    def __call__(self, name):
        return f"{self.greeting}, {name}!"

# Create a Greeter instance
greeter = Greeter("Hello")

# Call the Greeter instance like a function
print(greeter("Alice"))  # Output: Hello, Alice!
print(greeter("Bob"))    # Output: Hello, Bob!
