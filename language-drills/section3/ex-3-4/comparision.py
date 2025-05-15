from dataclasses import dataclass

@dataclass(frozen=True)
class User:
    name: str
    age: int

# Create two user instances
user1 = User("Alice", 30)
user2 = User("Alice", 30)
user3 = User("Bob", 25)

# Compare the users
print(user1 == user2)  # Output: True (same name and age)
print(user1 == user3)  # Output: False (different name and age)
