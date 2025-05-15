from collections import defaultdict

words = ['apple', 'banana', 'apricot', 'blueberry', 'cherry', 'avocado']

# Create a defaultdict with list as the default factory
grouped_words = defaultdict(list)

# Group words by their first letter
for word in words:
    first_letter = word[0]
    grouped_words[first_letter].append(word)

# Print the grouped words
for letter, group in grouped_words.items():
    print(f"{letter}: {group}")
