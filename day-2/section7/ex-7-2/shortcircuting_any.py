numbers = [123, 456, 789, 198, 297, 400]  

# Check if any number is divisible by 99
has_divisible_by_99 = any(num % 99 == 0 for num in numbers)

print(has_divisible_by_99)
