import time
from threading import Lock

metrics = {
    'function_calls': {},
    'errors': {},
    'execution_times': {},
}
metrics_lock = Lock()

from functools import wraps

def track_metrics(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        func_name = func.__name__
        start = time.perf_counter()
        with metrics_lock:
            metrics['function_calls'][func_name] = metrics['function_calls'].get(func_name, 0) + 1

        try:
            result = func(*args, **kwargs)
            return result
        except Exception as e:
            with metrics_lock:
                metrics['errors'][func_name] = metrics['errors'].get(func_name, 0) + 1
            raise e
        finally:
            duration = time.perf_counter() - start
            with metrics_lock:
                metrics['execution_times'].setdefault(func_name, []).append(duration)
    return wrapper

def get_metrics():
    with metrics_lock:
        return {
            'function_calls': dict(metrics['function_calls']),
            'errors': dict(metrics['errors']),
            'average_execution_times': {
                fn: round(sum(times)/len(times), 4)
                for fn, times in metrics['execution_times'].items()
            }
        }
@track_metrics
def fast_task():
    time.sleep(0.05)

@track_metrics
def error_task():
    time.sleep(0.1)
    raise ValueError("Oops")

# Simulate calls
for _ in range(3):
    fast_task()

try:
    error_task()
except:
    pass

# View metrics
import json
print(json.dumps(get_metrics(), indent=2))
