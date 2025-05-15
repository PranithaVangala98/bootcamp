from functools import reduce

# Factorial using reduce and lambda
def factorial(n):
    return reduce(lambda x, y: x * y, range(1, n + 1))

# Example usage
n = 5
print(f"Factorial of {n} is {factorial(n)}")
    