from dataclasses import dataclass, field

@dataclass
class User:
    name: str
    age: int
    country: str = "India"  # Default value for country

    def __post_init__(self):
        if self.age < 0:
            raise ValueError("Age cannot be negative")
        
# Example usage:
try:
    user1 = User(name="Alice", age=30)
    print(user1)

    user2 = User(name="Bob", age=-5)  # This will raise a ValueError
except ValueError as e:
    print(f"Error: {e}")
