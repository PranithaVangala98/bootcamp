def nested_try_example():
    try:
        num = int(input("Enter a number: "))
        try:
            result = 10 / num
            print("Result:", result)
        except ZeroDivisionError:
            print("Inner: Cannot divide by zero.")
    except ValueError:
        print("Outer: Invalid input. Please enter a valid number.")


nested_try_example()
