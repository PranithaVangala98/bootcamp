import itertools

data = [1, 2, 3]

# All ordered pairs (permutations of 2)
print("Permutations (pairs):")
for p in itertools.permutations(data, 2):
    print(p)

# All unordered pairs (combinations of 2)
print("\nCombinations (pairs):")
for c in itertools.combinations(data, 2):
    print(c)

# All unordered triples (combinations of 3)
print("\nCombinations (triples):")
for c in itertools.combinations(data, 3):
    print(c)

# All ordered triples (permutations of 3)
print("\nPermutations (triples):")
for p in itertools.permutations(data, 3):
    print(p)
