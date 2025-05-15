import platform
import psutil
import time

def health_check():
    return {
        'status': 'OK',
        'timestamp': time.strftime('%Y-%m-%d %H:%M:%S'),
        'system': platform.system(),
        'release': platform.release(),
        'uptime_minutes': round(time.time() - psutil.boot_time()) // 60,
        'cpu_usage_percent': psutil.cpu_percent(interval=0.5),
        'memory_usage_percent': psutil.virtual_memory().percent,
        'available_memory_mb': round(psutil.virtual_memory().available / (1024 * 1024), 2)
    }
if __name__ == '__main__':
    import json
    print(json.dumps(health_check(), indent=2))
