from dataclasses import dataclass

@dataclass(frozen=True)
class User:
    name: str
    age: int

    def is_adult(self) -> bool:
        """Returns True if age is 18 or greater, indicating an adult."""
        return self.age >= 18

# Create instances of User
user1 = User("Alice", 30)
user2 = User("Bob", 16)

# Test the is_adult method
print(f"Is {user1.name} an adult? {user1.is_adult()}")  # Output: True
print(f"Is {user2.name} an adult? {user2.is_adult()}")  # Output: False
