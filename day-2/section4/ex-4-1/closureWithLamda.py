def make_multiplier(factor):
    return lambda x: x * factor

# Example usage
multiply_by_3 = make_multiplier(3)
result = multiply_by_3(5)
print(result)  # Output: 15
