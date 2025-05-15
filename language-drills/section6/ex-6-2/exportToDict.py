from pydantic import BaseModel


class Profile(BaseModel):
    bio: str
    location: str


class User(BaseModel):
    name: str
    age: int
    profile: Profile


# Create an instance
user = User(name="Alice", age=30, profile=Profile(bio="Engineer", location="NYC"))

# Export as dict
user_dict = user.dict()
print("As dict:", user_dict)

# Export as JSON string
user_json = user.json()
print("As JSON:", user_json)
