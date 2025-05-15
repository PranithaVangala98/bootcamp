from pydantic import BaseModel, Field

class UserModel(BaseModel):
    """
    UserModel represents the data structure for a user.
    
    This model is used to store and validate the information of a user,
    including their unique identifier, email address, and full name.
    """

    id: int = Field(..., alias="user_id", title="User Identifier", example=123)
    email: str = Field(..., description="User's email address", example="user@example.com")
    name: str = Field(..., title="Full Name", example="John Doe")
