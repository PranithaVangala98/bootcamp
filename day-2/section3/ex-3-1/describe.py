class MyClass:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def describe(self):
        return f"My name is {self.name} and I am {self.age} years old."

# Example usage
person = MyClass("Alice", 30)
print(person.describe())
