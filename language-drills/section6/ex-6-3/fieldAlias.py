from pydantic import BaseModel, Field

class UserModel(BaseModel):
    id: int = Field(..., alias="user_id")

data = {"user_id": 123}
user = UserModel(**data)
print(user.id)  # Outputs: 123

user_dict = user.dict(by_alias=True)
print(user_dict)  # Outputs: {'user_id': 123}
