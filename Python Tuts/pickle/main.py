import pickle

# Example data (a simple dictionary)
data = {'name': 'John', 'age': 30, 'city': 'New York'}

# Pickle the data (serialize)
with open('data.pickle', 'wb') as file:
    pickle.dump(data, file)

# Unpickle the data (deserialize)
with open('data.pickle', 'rb') as file:
    loaded_data = pickle.load(file)

print(loaded_data)

sterilized_data = pickle.dumps(data)
print(sterilized_data)
print(pickle.loads(sterilized_data))

# PLEASE NOTE THAT THE PICKLE DATABASES ARE CREATED IN PYTHON DUMP FILE DIRECTORY BECAUSE TERMINAL WAS OPEN THERE