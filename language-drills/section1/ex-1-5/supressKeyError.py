from contextlib import suppress

thisdict = {"a": 1, "b": 2}

with suppress(KeyError):
    print(thisdict["d"])

print("Program continues...")
