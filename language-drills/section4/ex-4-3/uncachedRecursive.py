import time
from functools import lru_cache

# Recursive Fibonacci without lru_cache
def fib_uncached(n):
    if n <= 1:
        return n
    return fib_uncached(n - 1) + fib_uncached(n - 2)

# Recursive Fibonacci with lru_cache
@lru_cache(None)
def fib_cached(n):
    if n <= 1:
        return n
    return fib_cached(n - 1) + fib_cached(n - 2)

# Compare performance
n = 35  # Test with a larger number to see a performance difference

# Measure time for uncached version
start_time = time.time()
fib_uncached(n)
uncached_time = time.time() - start_time

# Measure time for cached version
start_time = time.time()
fib_cached(n)
cached_time = time.time() - start_time

print(f"Uncached Fibonacci time: {uncached_time:.6f} seconds")
print(f"Cached Fibonacci time: {cached_time:.6f} seconds")
