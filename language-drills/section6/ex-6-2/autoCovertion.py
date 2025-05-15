from pydantic import BaseModel, conint


class User(BaseModel):
    name: str
    age: conint(gt=0)


# Input where age is a string
data = {
    "name": "Alice",
    "age": "42",  # string input
}

user = User(**data)
print(user)
print(f"Type of age: {type(user.age)}")
