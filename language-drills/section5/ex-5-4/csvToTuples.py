import csv
from collections import namedtuple

# Define the namedtuple type based on the CSV header
Row = namedtuple('Row', ['name', 'age', 'city'])

# Open the CSV file and read its contents
with open('data.csv', mode='r', newline='') as file:
    reader = csv.reader(file)
    
    # Skip the header (optional, if present)
    next(reader)
    
    # Read each row and convert it to a namedtuple
    for row in reader:
        # Convert row to namedtuple using the defined field names
        named_row = Row(*row)
        
        # Print the namedtuple (you can access each field by name)
        print(named_row)
        print(f"Name: {named_row.name}, Age: {named_row.age}, City: {named_row.city}")
