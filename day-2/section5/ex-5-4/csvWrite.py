import csv

# List of dictionaries to be written to the CSV
data = [
    {'name': 'Alice', 'age': 30, 'city': 'New York'},
    {'name': 'Bob', 'age': 25, 'city': 'Los Angeles'},
    {'name': 'Charlie', 'age': 35, 'city': 'Chicago'}
]

# Define the CSV file path
csv_file = 'output.csv'

# Open the CSV file in write mode
with open(csv_file, mode='w', newline='') as file:
    # Create a DictWriter object and write the header
    fieldnames = ['name', 'age', 'city']
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    
    # Write the header
    writer.writeheader()
    
    # Write the rows of data
    writer.writerows(data)

print(f"Data has been written to {csv_file}")
