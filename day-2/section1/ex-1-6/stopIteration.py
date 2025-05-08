def manual_iterator():
    raise StopIteration("No more items.")

try:
    manual_iterator()
except StopIteration as e:
    print(f"Caught StopIteration: {e}")