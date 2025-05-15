from functools import wraps
import logging
import json

# Configure basic logging
logging.basicConfig(level=logging.INFO, format='[TRACE] %(message)s')
logger = logging.getLogger(__name__)

def trace_calls(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        arg_list = [repr(a) for a in args]
        kwarg_list = [f"{k}={v!r}" for k, v in kwargs.items()]
        all_args = ", ".join(arg_list + kwarg_list)

        logger.info(f"Calling {func.__name__}({all_args})")
        result = func(*args, **kwargs)
        logger.info(f"{func.__name__} returned {result!r}")
        return result
    return wrapper
@trace_calls
def add(a, b):
    return a + b

@trace_calls
def greet(name="World"):
    return f"Hello, {name}!"

add(5, 7)
greet(name="Alice")
