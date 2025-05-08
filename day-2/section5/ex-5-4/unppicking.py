import json

# Define a simple Python object (dictionary)
data = {
    'name': 'Alice',
    'age': 30,
    'city': 'New York'
}

# Serialize (convert to JSON string)
with open('data.json', 'w') as file:
    json.dump(data, file)

print("Object has been serialized to 'data.json'.")

# Deserialize (convert from JSON string back to Python object)
with open('data.json', 'r') as file:
    loaded_data = json.load(file)

print("Object has been deserialized:", loaded_data)
