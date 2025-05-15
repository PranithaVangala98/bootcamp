import timeit

# Time the execution of sum(range(10000))
execution_time = timeit.timeit('sum(range(10000))', number=1000)

# Print the execution time
print(f"Execution time: {execution_time} seconds")
