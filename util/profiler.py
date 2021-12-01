import time

def profile(func):
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        value = func(*args, **kwargs)
        end = time.perf_counter()
        print(f"- Completion Time: {round(end - start, 5)}sec")
        return value
    return wrapper