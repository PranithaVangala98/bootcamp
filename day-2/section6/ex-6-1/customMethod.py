from dataclasses import dataclass

@dataclass(frozen=True)
class User:
    name: str
    age: int
    country: str = "India"

    def is_adult(self) -> bool:
        return self.age >= 18

# Example usage:
user1 = User(name="Alice", age=30)
user2 = User(name="Bob", age=16)

print(f"{user1.name} is an adult: {user1.is_adult()}")
print(f"{user2.name} is an adult: {user2.is_adult()}")
