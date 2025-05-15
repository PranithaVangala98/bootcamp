import traceback
def dividefunc(a, b):
    try:
        return a / b
    except Exception:
        #capture and print the full traceback as a string
        error_trace = traceback.format_exc()
        print("An error occurred:")
        print(error_trace)

dividefunc(10, 0)
