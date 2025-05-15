def filter_rows(data, condition):
    for row in data:
        if condition(row):
            yield row
data = [
    {"name": "Alice", "age": 25},
    {"name": "Bob", "age": 35},
    {"name": "Charlie", "age": 40}
]

#filter condition
def age_over_30(row):
    return row["age"] > 30

#generator
filtered = filter_rows(data, age_over_30)


for row in filtered:
    print(row)
