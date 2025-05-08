import itertools

# Create an infinite ID generator starting from 1
id_generator = itertools.count(start=1)

# Generate the first 10 IDs as an example
for _ in range(10):
    print(next(id_generator))
