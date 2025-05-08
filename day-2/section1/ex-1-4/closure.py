def make_multiplier(n):
    def multiply(y):
        return n * y

    return multiply


triple = make_multiplier(3)
print(triple(10))
