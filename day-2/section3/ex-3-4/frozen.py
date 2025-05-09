from dataclasses import dataclass

@dataclass(frozen=True)
class User:
    name: str
    age: int

# Create an instance of User
user1 = User("Alice", 30)

# Print the user instance
print(user1)  # Output: User(name='Alice', age=30)

# Attempting to modify the attributes will raise a FrozenInstanceError
try:
    user1.age = 35  # This will raise an error
except AttributeError as e:
    print(f"Error: {e}")
