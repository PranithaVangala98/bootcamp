import functools

# Step 1: Define a partial function to fix the 'end' parameter
custom_print = functools.partial(print, end="... ")

# Step 2: Define another partial function to fix the 'sep' parameter
custom_print = functools.partial(custom_print, sep=" | ")

# Step 3: Add a prefix by chaining another partial
custom_print = functools.partial(custom_print, "Prefix:")

# Step 4: Use the customized print function
custom_print("Hello", "World")  # Output: Prefix:Hello | World... 
