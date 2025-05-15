import pdb

def calculate_total(price, quantity):
    total = price * quantity
    pdb.set_trace()
    return total

result = calculate_total(10, 5)
print("Total:", result)
