import timeit

# Time for list comprehension
list_time = timeit.timeit('[x*x for x in range(1000000)]', number=100)

# Time for generator expression
generator_time = timeit.timeit('(x*x for x in range(1000000))', number=100)

# Print the results
print(f"List comprehension time: {list_time} seconds")
print(f"Generator expression time: {generator_time} seconds")
