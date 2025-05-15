import csv

# Open the CSV file and read its contents
with open('data.csv', mode='r', newline='') as file:
    reader = csv.DictReader(file)
    
    # Iterate through each row in the CSV and print it
    for row in reader:
        print(row)
