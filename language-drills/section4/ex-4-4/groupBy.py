import itertools

# Sample list of dicts
items = [
    {'category': 'fruit', 'name': 'apple'},
    {'category': 'fruit', 'name': 'banana'},
    {'category': 'vegetable', 'name': 'carrot'},
    {'category': 'fruit', 'name': 'mango'},
    {'category': 'vegetable', 'name': 'spinach'}
]

# Sort by 'category' so groupby can group properly
items.sort(key=lambda x: x['category'])

# Group by 'category'
for key, group in itertools.groupby(items, key=lambda x: x['category']):
    print(f"{key}:")
    for item in group:
        print(f"  {item}")
