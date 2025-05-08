import json

# Define a Python dictionary
data = {
    "name": "Alice",
    "age": 30,
    "city": "New York",
    "job": "Engineer"
}

# Serialize the Python dictionary to a JSON string with indentation and sorted keys
json_data = json.dumps(data, indent=4, sort_keys=True)

# Output the pretty-printed JSON string
print("Pretty-printed JSON:")
print(json_data)
