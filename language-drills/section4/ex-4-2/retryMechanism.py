import time


def retry(max_retries=3, delay=1):
    def decorator(func):
        def wrapper(*args, **kwargs):
            attempts = 0
            while attempts < max_retries:
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    attempts += 1
                    print(f"Attempt {attempts} failed: {e}")
                    if attempts < max_retries:
                        print(f"Retrying in {delay} seconds...")
                        time.sleep(delay)
                    else:
                        print("Max retries reached. Function failed.")
                        raise

        return wrapper

    return decorator


@retry(max_retries=5, delay=2)
def unreliable_function():
    print("Attempting operation...")
    if time.time() % 2 < 1:
        raise ValueError("Random failure!")
    return "Success!"


# Call the decorated function
try:
    result = unreliable_function()
    print(result)
except Exception as e:
    print(f"Function ultimately failed: {e}")
