class MyClass:
    def __init__(self, name="John", age=25):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}"


obj = MyClass()
print(obj)  


obj.city = "New York"


print(f"City: {obj.city}") 