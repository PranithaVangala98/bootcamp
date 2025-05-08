x = 5  # Global variable


def modify_global():
    global x
    x += 10
    print("Inside function, x =", x)


modify_global()
print("Outside function, x =", x)
