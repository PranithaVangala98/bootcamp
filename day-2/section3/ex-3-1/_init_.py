class MyClass:
    def __init__(self, name="John", age=25):
  
        self.name = name
        self.age = age

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}"


obj1 = MyClass()
print(obj1)  


obj2 = MyClass(name="Alice", age=30)
print(obj2)  

obj3 = MyClass(name="Bob")
print(obj3)  
