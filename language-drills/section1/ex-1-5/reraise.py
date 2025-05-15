def divide(a, b):
    result = a / b
    print("result", result)


# Test
try:
    divide(10, 0)
except ZeroDivisionError as e:
    print("Caught again in outer block:", e)
    raise
