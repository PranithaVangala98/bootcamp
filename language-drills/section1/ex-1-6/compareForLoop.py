def square_generator():
    for i in range(1, 6):
        yield i**2


gen = square_generator()
print("Generator output:", list(gen))

squares_lc = [i**2 for i in range(1, 6)]
print("List comprehension output:", squares_lc)
