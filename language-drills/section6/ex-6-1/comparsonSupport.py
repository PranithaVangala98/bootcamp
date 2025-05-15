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

# Create two User instances
user1 = User(name="Alice", age=30)
user2 = User(name="Alice", age=30)

# Compare the two instances
print(user1 == user2)  # True

# Create another user with different attributes
user3 = User(name="Alice", age=30, tags=["developer"])

print(user1 == user3)  # False, because tags are different
