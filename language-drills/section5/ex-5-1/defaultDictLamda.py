from collections import defaultdict

# Create a defaultdict with a lambda for default value "N/A"
my_dict = defaultdict(lambda: "N/A")

# Access existing and missing keys
print(my_dict["existing_key"])  # This will return the default value "N/A"
print(my_dict["another_key"])   # This will also return "N/A"

# Add a key-value pair
my_dict["name"] = "John"
print(my_dict["name"])  # Output: John
