class Profile:
    def __init__(self, bio: str, location: str):
        self.bio = bio
        self.location = location

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            bio=data.get('bio', ''),
            location=data.get('location', '')
        )

    def __repr__(self):
        return f"Profile(bio={self.bio!r}, location={self.location!r})"


class User:
    def __init__(self, name: str, age: int, profile: Profile):
        self.name = name
        self.age = age
        self.profile = profile

    @classmethod
    def from_dict(cls, data: dict):
        try:
            name = data.get('name', '')
            age = int(data.get('age'))
            profile_data = data.get('profile', {})
            profile = Profile.from_dict(profile_data)
            return cls(name=name, age=age, profile=profile)
        except (ValueError, TypeError) as e:
            raise ValueError(f"Invalid data for User: {e}")

    def __repr__(self):
        return f"User(name={self.name!r}, age={self.age!r}, profile={self.profile!r})"
