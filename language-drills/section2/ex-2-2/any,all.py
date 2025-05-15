numbers = [3, 5, -2, 7, 10]


has_negative = any(n < 0 for n in numbers)
print(f"Any negative? {has_negative}")


all_positive = all(n > 0 for n in numbers)
print(f"All positive? {all_positive}")
