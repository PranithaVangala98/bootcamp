def validate_args(func):
    def wrapper(self, *args, **kwargs):
        # Perform validation on the arguments
        for arg in args:
            if not isinstance(
                arg, int
            ):  # Example validation: Check if arguments are integers
                raise ValueError(f"Invalid argument: {arg} is not an integer")

        for key, value in kwargs.items():
            if not isinstance(value, int):  # Example validation for keyword arguments
                raise ValueError(f"Invalid argument: {key}={value} is not an integer")

        return func(self, *args, **kwargs)

    return wrapper


class Calculator:
    @validate_args
    def add(self, a, b):
        return a + b

    @validate_args
    def multiply(self, a, b):
        return a * b


# Create an instance of the Calculator class
calc = Calculator()

# Call the methods with valid arguments
print(calc.add(3, 4))  # Should work
print(calc.multiply(2, 5))  # Should work

# Call the methods with invalid arguments
try:
    print(calc.add(3, "4"))  # This should raise an error
except ValueError as e:
    print(e)

try:
    print(calc.multiply("2", 5))  # This should raise an error
except ValueError as e:
    print(e)
