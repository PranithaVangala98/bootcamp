def mixed_function(*args, **kwargs):
    print("Positional arguments (args):", args)
    for key, value in kwargs.items():
        print(f"{key}: {value}")


mixed_function(1, 2, 3, a=10, b=20)
