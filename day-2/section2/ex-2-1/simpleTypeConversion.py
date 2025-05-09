user_input = input("Enter a number: ")

try:
    number = int(user_input)
    print(f"Valid integer: {number}")
except ValueError:
    print("Invalid input! Please enter a valid integer.")
