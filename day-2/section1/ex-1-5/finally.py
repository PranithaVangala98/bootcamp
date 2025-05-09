try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide")
finally:
    print("Cleanup done")
