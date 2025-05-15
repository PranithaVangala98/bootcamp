from dataclasses import dataclass

@dataclass
class User:
    name: str
    age: int
    country: str = "India"  # Default value for country

# Example usage:
user1 = User(name="Alice", age=30)
user2 = User(name="Bob", age=25, country="USA")

print(user1)
print(user2)
