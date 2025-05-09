def outer():
    message = "Hello!"

    def inner():
        print(message)  # Accessing the outer function's variable

    inner()


outer()
