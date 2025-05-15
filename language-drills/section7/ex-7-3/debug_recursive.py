def factorial(n, level=0):
    indent = "  " * level  # Two spaces per level
    print(f"{indent}Entering factorial({n})")

    if n == 0 or n == 1:
        print(f"{indent}Returning 1")
        return 1

    result = n * factorial(n - 1, level + 1)
    print(f"{indent}Returning {result} from factorial({n})")
    return result

factorial(4)
