a = {1, 2, 3}
b = {3, 4}


def setOperations(a, b):
    intersection = a & b
    union = a | b
    difference = a - b
    print(union)
    print(intersection)
    print(difference)


setOperations(a, b)
