import sys

# A list of numbers
list_obj = [x for x in range(1000)]
# A generator that yields numbers
gen_obj = (x for x in range(1000))

print("List size:", sys.getsizeof(list_obj))     # Size of the entire list
print("Generator size:", sys.getsizeof(gen_obj)) # Only the generator object itself
