try:
    x = 10 / 0  # This will raise ZeroDivisionError
except Exception as e:
    print(type(e), e)
