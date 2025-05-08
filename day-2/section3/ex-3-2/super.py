class Animal:
    def describe(self):
        print("This is an animal.")


class Dog(Animal):
    def describe(self):
        # Call the parent class's describe method
        super().describe()
        print("This is a dog.")


my_dog = Dog()
my_dog.describe()
