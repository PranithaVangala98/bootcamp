from collections import Counter

numbers = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5]

# Count frequencies
counter = Counter(numbers)

# Get the 2 most common elements
most_common_two = counter.most_common(2)

print(most_common_two)
