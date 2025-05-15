import json

# Define a Python dictionary
data = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}

# Serialize the Python dictionary to a JSON string using json.dumps()
json_data = json.dumps(data)

# Output the serialized JSON string
print("Serialized JSON:", json_data)

# Deserialize the JSON string back to a Python dictionary using json.loads()
deserialized_data = json.loads(json_data)

# Output the deserialized Python dictionary
print("Deserialized Python dictionary:", deserialized_data)
