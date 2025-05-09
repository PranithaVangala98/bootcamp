from pydantic import BaseModel, Field

class UserModel(BaseModel):
    email: str = Field(..., description="User's email address")
