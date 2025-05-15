class MyClass:
    @staticmethod
    def static_method(arg):
        """A simple static method that prints the argument."""
        print(f"Static method called with argument: {arg}")

# Calling static method from the class
MyClass.static_method("Hello from class!")

# Creating an instance of MyClass
obj = MyClass()

# Calling static method from the instance
obj.static_method("Hello from instance!")
