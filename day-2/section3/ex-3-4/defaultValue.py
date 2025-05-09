from dataclasses import dataclass

@dataclass
class User:
    name: str
    age: int = 0  # Default value for age is 0

# Create instances of User
user1 = User("Alice", 30)
user2 = User("Bob")  # age will default to 0

# Print the user instances
print(user1)  # Output: User(name='Alice', age=30)
print(user2)  # Output: User(name='Bob', age=0)
