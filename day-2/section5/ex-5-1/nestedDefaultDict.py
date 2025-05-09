from collections import defaultdict

# Create a defaultdict where the default value is a dict
nested_dict = defaultdict(dict)

# Add hierarchical data
nested_dict["fruit"]["apple"] = 5
nested_dict["fruit"]["banana"] = 10
nested_dict["vegetable"]["carrot"] = 3

# Access hierarchical data
print(nested_dict)
