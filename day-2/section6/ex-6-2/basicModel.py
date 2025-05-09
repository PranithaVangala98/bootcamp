class User:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            name=data.get('name', ''),
            age=int(data.get('age', 0))
        )

    def __repr__(self):
        return f"User(name={self.name!r}, age={self.age!r})"
