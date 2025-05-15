numbers = [1, 2, 3, 4, 5, 6]


doubled_numbers = list(map(lambda x: x * 2, numbers))
print(f"Doubled numbers: {doubled_numbers}")


odd_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(f"Odd numbers (removed evens): {odd_numbers}")
