from dataclasses import dataclass, field
from typing import List

@dataclass(frozen=True)
class User:
    name: str
    age: int
    country: str = "India"
    tags: List[str] = field(default_factory=list)

    def is_adult(self) -> bool:
        return self.age >= 18

# Example usage:
user1 = User(name="Alice", age=30)
user2 = User(name="Bob", age=16, tags=["student", "athlete"])

print(f"{user1.name} has tags: {user1.tags}")
print(f"{user2.name} has tags: {user2.tags}")

# Adding tags after creation will not work due to the frozen=True decorator.
