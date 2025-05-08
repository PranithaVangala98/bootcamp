from dataclasses import dataclass

@dataclass(frozen=True)
class User:
    name: str
    age: int
    country: str = "India"

# Example usage:
user1 = User(name="Alice", age=30)

print(user1)

# Trying to modify a field will raise a FrozenInstanceError
try:
    user1.age = 35  # This will raise an error
except AttributeError as e:
    print(f"Error: {e}")
