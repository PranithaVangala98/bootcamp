from collections import OrderedDict

# Create an OrderedDict
ordered = OrderedDict()

# Insert items in a specific order
ordered['apple'] = 1
ordered['banana'] = 2
ordered['cherry'] = 3

# Iterate while preserving insertion order
for key, value in ordered.items():
    print(f"{key}: {value}")
