from pydantic import BaseModel, conint, constr, validator


class Profile(BaseModel):
    bio: str
    location: str


class User(BaseModel):
    name: constr(min_length=3)
    age: conint(gt=0)
    profile: Profile

    @validator("name")
    def name_must_be_capitalized(cls, v):
        if not v[0].isupper():
            raise ValueError("Name must start with an uppercase letter")
        return v
