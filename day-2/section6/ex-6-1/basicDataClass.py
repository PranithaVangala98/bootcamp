from dataclasses import dataclass

@dataclass
class User:
    name: str
    age: int

# Example usage:
user1 = User(name="Alice", age=30)
print(user1)
