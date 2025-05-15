filename = "adhaarcard.txt"

try:
    with open(filename, 'r') as file:
        content = file.read()
        print("File content:")
        print(content)
except FileNotFoundError:
    print(f"Error: The file '{filename}' was not found.")