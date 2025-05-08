user = {"name": "Alice", "location": "hyderbad"}


def dictAccess(user):
    name = user.get("name")
    print("name", name)
    age = user.setdefault("age", "24")
    print(age)
    print(user)


dictAccess(user)
