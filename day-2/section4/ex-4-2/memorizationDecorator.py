def memoize(func):
    cache = {}  # Dictionary to store the cached results

    def wrapper(*args):
        if args in cache:
            print(f"Returning cached result for {args}")
            return cache[args]
        else:
            result = func(*args)
            cache[args] = result  # Store the result in the cache
            return result

    return wrapper


@memoize
def slow_add(a, b):
    print(f"Computing {a} + {b}...")
    return a + b


# Call the decorated function
print(slow_add(3, 4))  # This will compute and cache the result
print(slow_add(3, 4))  # This will return the cached result
print(slow_add(5, 6))  # This will compute and cache a new result
