user = {"name": "Alice", "location": "hyderbad", "age": "24"}


def dictIteration(user):
    for k, v in user.items():
        print(k, v)


dictIteration(user)
