import logging
import time
from functools import wraps

# Basic logger setup
logging.basicConfig(
    level=logging.INFO,
    format='[UserID: %(user_id)s] [Function: %(funcName)s] [Duration: %(duration).3fs] %(message)s'
)

# Custom LoggerAdapter
class ContextLoggerAdapter(logging.LoggerAdapter):
    def process(self, msg, kwargs):
        return msg, {**kwargs, 'extra': {**self.extra, **kwargs.get('extra', {})}}

def get_logger(user_id):
    return ContextLoggerAdapter(logging.getLogger(__name__), {'user_id': user_id, 'duration': 0.0})

# Decorator to log timing
def log_with_timing(user_id):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            logger = get_logger(user_id)
            start = time.perf_counter()
            result = func(*args, **kwargs)
            duration = time.perf_counter() - start
            logger.info('Function executed.', extra={'duration': duration})
            return result
        return wrapper
    return decorator

@log_with_timing('u123')
def slow_function():
    time.sleep(1.5)  # Simulate slowness

@log_with_timing('u456')
def fast_function():
    return sum(range(100))

slow_function()
fast_function()
