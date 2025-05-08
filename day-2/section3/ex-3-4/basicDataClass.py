from dataclasses import dataclass

@dataclass
class User:
    name: str
    age: int

# Create an instance of User
user1 = User("Alice", 30)
user2 = User("Bob", 25)

# Print the user instances
print(user1)  # Output: User(name='Alice', age=30)
print(user2)  # Output: User(name='Bob', age=25)
