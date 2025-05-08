class Animal:
    def __init__(self, name):
        self.name = name

    def sound(self):
        raise NotImplementedError("Subclasses must implement this method")


class Dog(Animal):
    def sound(self):
        return "Woof!"


a = Animal("Generic Animal")


d = Dog("Buddy")


print(a.name)
print(d.name)
print(d.sound())
