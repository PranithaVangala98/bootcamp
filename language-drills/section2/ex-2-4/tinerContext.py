import time
from contextlib import contextmanager

@contextmanager
def timer():
    start = time.time()
    print("Timer started")
    try:
        yield
    finally:
        end = time.time()
        print(f"Timer ended: {end - start:.4f} seconds")

# Using the timer context manager
with timer():
    # Simulate some work
    time.sleep(2)
