def running_totals(numbers):
    total = 0
    for num in numbers:
        total += num
        yield total
data = [1, 2, 3, 4]
for total in running_totals(data):
    print(total)