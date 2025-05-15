import logging
from functools import wraps

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

#decorator for logging
def log_entry_exit(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        logger.debug(f"Entering: {func.__name__}() with args={args}, kwargs={kwargs}")
        result = func(*args, **kwargs)
        logger.debug(f"Exiting : {func.__name__}() with result={result}")
        return result
    return wrapper

# Use the decorator
@log_entry_exit
def add(a, b):
    return a + b

# Example call
add(3, 5)
