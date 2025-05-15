from functools import lru_cache

@lru_cache(None)  # None means there's no limit on the cache size
def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)

# Example usage
print(fib(10))  # Output: 55
