def collect_numbers():
    numbers = []
    for i in range(5):
        numbers.append(i)
    return numbers

result = collect_numbers()
print(result)  


def generate_numbers():
    for i in range(5):
        yield i

result = generate_numbers()
print(list(result))  
