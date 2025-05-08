from pydantic import BaseModel, Field

class UserModel(BaseModel):
    id: int = Field(..., alias="user_id", title="User Identifier", example=123)
    email: str = Field(..., description="User's email address", example="user@example.com")
    name: str = Field(..., title="Full Name", example="John Doe")
data = {"user_id": 123, "email": "user@example.com", "name": "John Doe"}
user = UserModel(**data)

print(user)
