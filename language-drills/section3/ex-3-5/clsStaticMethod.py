class MyClass:
    class_variable = "I'm a class variable!"

    def __init__(self, instance_variable):
        self.instance_variable = instance_variable

    @staticmethod
    def static_method():
        # Static method does not have access to self or cls
        print("This is a static method.")
        # Uncommenting the next line will cause an error because `self` and `cls` are not available:
        # print(self.instance_variable)  # Error: name 'self' is not defined
        # print(cls.class_variable)  # Error: name 'cls' is not defined

    @classmethod
    def class_method(cls):
        # Class method has access to `cls`
        print("This is a class method.")
        print(f"Accessing class variable via cls: {cls.class_variable}")

    def instance_method(self):
        # Instance method has access to `self`
        print(f"This is an instance method. Accessing instance variable: {self.instance_variable}")


# Create an instance of MyClass
obj = MyClass("I'm an instance variable!")

# Call static method (no access to instance or class)
MyClass.static_method()  # Output: This is a static method.

# Call class method (accesses the class)
MyClass.class_method()  # Output: This is a class method. Accessing class variable via cls: I'm a class variable!

# Call instance method (accesses the instance)
obj.instance_method()  # Output: This is an instance method. Accessing instance variable: I'm an instance variable!
