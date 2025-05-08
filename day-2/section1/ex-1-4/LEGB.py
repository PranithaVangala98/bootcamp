x = 10  # Global variable


def my_function():
    x = 20  # Local variable
    print("Local x:", x)


my_function()
print("Global x:", x)
