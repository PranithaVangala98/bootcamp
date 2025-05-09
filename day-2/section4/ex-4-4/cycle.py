import itertools

# Define the pattern
colors = ["red", "green", "blue"]

# Create a cycle generator
color_cycle = itertools.cycle(colors)

# Print the first 6 items from the cycle
for _ in range(6):
    print(next(color_cycle))
