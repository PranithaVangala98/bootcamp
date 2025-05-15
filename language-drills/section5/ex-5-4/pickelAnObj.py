import pickle

# Define a basic Python object (dictionary in this case)
data = {
    'name': 'Alice',
    'age': 30,
    'city': 'New York'
}

# Serialize (pickle) the object to a file
with open('data.pkl', 'wb') as file:
    pickle.dump(data, file)

print("Object has been pickled to 'data.pkl'.")

# Deserialize (unpickle) the object from the file
with open('data.pkl', 'rb') as file:
    loaded_data = pickle.load(file)

print("Object has been unpickled:", loaded_data)
