import functools

# Create a partial function to generate a dictionary with default value as a new dictionary
nested_dict = functools.partial(dict, **{'__missing__': lambda key: {}})

# Example usage
my_dict = nested_dict()

# Adding nested values
my_dict['a']['b']['c'] = 1

print(my_dict)  # Output: {'a': {'b': {'c': 1}}}
