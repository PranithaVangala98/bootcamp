import os
import logging
import time
from functools import wraps

# Check DEBUG mode from environment
DEBUG_MODE = os.getenv('DEBUG', 'False').lower() in ('true', '1')

# Configure logging level based on DEBUG flag
logging.basicConfig(
    level=logging.DEBUG if DEBUG_MODE else logging.INFO,
    format='[UserID: %(user_id)s] [Function: %(funcName)s] [Duration: %(duration).3fs] [ErrorID: %(error_id)s] %(message)s'
)

class ContextLoggerAdapter(logging.LoggerAdapter):
    def process(self, msg, kwargs):
        extra = self.extra.copy()
        extra.update(kwargs.get('extra', {}))
        kwargs['extra'] = extra
        return msg, kwargs

def get_logger(user_id):
    return ContextLoggerAdapter(logging.getLogger(__name__), {
        'user_id': user_id,
        'duration': 0.0,
        'error_id': '-'
    })

# Decorator to log with context, timing, and error ID
def log_with_context(user_id, error_id='-'):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            logger = get_logger(user_id)
            start = time.perf_counter()
            try:
                logger.debug('Starting function execution...', extra={'error_id': error_id})
                result = func(*args, **kwargs)
                duration = time.perf_counter() - start
                logger.info('Function executed successfully.', extra={'duration': duration, 'error_id': error_id})
                return result
            except Exception as e:
                duration = time.perf_counter() - start
                logger.error(f'Exception occurred: {e}', extra={'duration': duration, 'error_id': error_id})
                if DEBUG_MODE:
                    logger.exception('Stack trace:')
                raise
        return wrapper
    return decorator

@log_with_context('u123', error_id='E1003')
def risky_operation():
    time.sleep(0.1)
    return 10 / 0  # This will trigger an exception

@log_with_context('u456', error_id='E1004')
def quick_task():
    time.sleep(0.05)

try:
    risky_operation()
except ZeroDivisionError:
    pass

quick_task()
