import itertools


numbers = range(10)

result = list(itertools.islice(numbers, 3, 7))


print(result)
