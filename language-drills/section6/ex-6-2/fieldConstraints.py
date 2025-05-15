from pydantic import BaseModel, Field
from pydantic.types import conint, constr


class User(BaseModel):
    username: constr(min_length=3) = Field(..., description="At least 3 characters")
    age: conint(gt=0) = Field(..., description="Must be positive")


# Example usage
try:
    valid_user = User(username="Alice", age=30)
    print("Valid:", valid_user)
except Exception as e:
    print("Error (Valid):", e)

try:
    invalid_user_name = User(username="Al", age=25)
    print("Valid:", invalid_user_name)
except Exception as e:
    print("Error (Short Username):", e)

try:
    invalid_user_age = User(username="Bob", age=0)
    print("Valid:", invalid_user_age)
except Exception as e:
    print("Error (Non-Positive Age):", e)
