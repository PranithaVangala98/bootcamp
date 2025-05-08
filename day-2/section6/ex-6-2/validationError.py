class User:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    @classmethod
    def from_dict(cls, data: dict):
        try:
            name = data.get('name', '')
            age = int(data.get('age'))  # This will raise ValueError if invalid
            return cls(name=name, age=age)
        except (ValueError, TypeError) as e:
            raise ValueError(f"Invalid data for User: {e}")

    def __repr__(self):
        return f"User(name={self.name!r}, age={self.age!r})"
