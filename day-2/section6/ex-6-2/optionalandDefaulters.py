from pydantic import BaseModel
from typing import Optional


class Profile(BaseModel):
    bio: Optional[str] = None  # nullable field with default None
    location: str


class User(BaseModel):
    name: str
    age: int
    profile: Profile


# Create an instance with the nullable field being None
user = User(
    name="Alice",
    age=30,
    profile=Profile(location="NYC"),  # bio is not provided, so it defaults to None
)

print(user)
