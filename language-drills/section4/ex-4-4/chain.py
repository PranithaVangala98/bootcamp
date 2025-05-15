import itertools

# Define the lists
list1 = [1, 2]
list2 = [3, 4]
list3 = [5]

# Use chain to flatten the lists
combined = itertools.chain(list1, list2, list3)

# Convert to a list and print the result
flattened_list = list(combined)
print(flattened_list)
