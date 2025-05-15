import os

filename = "data.txt"

# LBYL approach: Check first, then act
if os.path.exists(filename):
    with open(filename, 'r') as file:
        contents = file.read()
