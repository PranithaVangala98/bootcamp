import logging
import time
from functools import wraps

# Configure logger with error_id and duration support
logging.basicConfig(
    level=logging.INFO,
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

# Decorator to log function execution time and optionally error code
def log_with_context(user_id, error_id='-'):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            logger = get_logger(user_id)
            start = time.perf_counter()
            try:
                result = func(*args, **kwargs)
                duration = time.perf_counter() - start
                logger.info('Function executed successfully.', extra={'duration': duration, 'error_id': error_id})
                return result
            except Exception as e:
                duration = time.perf_counter() - start
                logger.error(f'Exception occurred: {e}', extra={'duration': duration, 'error_id': error_id})
                raise
        return wrapper
    return decorator

@log_with_context(user_id='u123', error_id='E1001')
def safe_divide():
    return 10 / 0  # Triggers ZeroDivisionError

@log_with_context(user_id='u456', error_id='E1002')
def successful_task():
    time.sleep(0.2)

try:
    safe_divide()
except ZeroDivisionError:
    pass

successful_task()
    