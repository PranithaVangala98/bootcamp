import itertools

# Original iterator
original = iter([10, 20, 30, 40])

# Duplicate the iterator into two independent ones
it1, it2 = itertools.tee(original)

# Iterate over both independently
print("Iterator 1:")
for item in it1:
    print(item)

print("Iterator 2:")
for item in it2:
    print(item)
