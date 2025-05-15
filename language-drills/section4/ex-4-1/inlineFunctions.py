def compose(f, g):
    return lambda x: f(g(x))
def square(x):
    return x * x

def add_three(x):
    return x + 3

# Compose the functions
composed_function = compose(square, add_three)

# Apply the composed function to a value
result = composed_function(4)
print(result)  # Output: 49
