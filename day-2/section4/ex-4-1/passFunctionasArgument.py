def apply(func, value):
    return func(value)

def square(x):

    return x * x

result = apply(square, 5)
print(result)  # Output: 25
