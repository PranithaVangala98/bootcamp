from dataclasses import dataclass, field
from typing import List

@dataclass(slots=True, frozen=True)
class User:
    name: str
    age: int
    country: str = "India"
    tags: List[str] = field(default_factory=list)

    def is_adult(self) -> bool:
        return self.age >= 18

# Example usage:
user = User(name="Alice", age=30)
print(user)
