import os

import psutil

def print_resource_usage():
    cpu_percent = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory()
    
    print(f"CPU Usage       : {cpu_percent:.2f}%")
    print(f"Memory Usage    : {memory.percent:.2f}%")
    print(f"Total Memory    : {round(memory.total / (1024**3), 2)} GB")
    print(f"Available Memory: {round(memory.available / (1024**3), 2)} GB")
    print(f"Used Memory     : {round(memory.used / (1024**3), 2)} GB")

def print_load_average():
    if hasattr(os, 'getloadavg'):
        load1, load5, load15 = os.getloadavg()
        print(f"Load Average (1m) : {load1:.2f}")
        print(f"Load Average (5m) : {load5:.2f}")
        print(f"Load Average (15m): {load15:.2f}")
    else:
        print("os.getloadavg() not supported on this platform.")


print("=== Resource Usage ===")
print_resource_usage()

print("\n=== Load Average ===")
print_load_average()
