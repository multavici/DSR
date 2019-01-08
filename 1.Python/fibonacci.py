from functools import lru_cache

@lru_cache()
def fib(x):
    if x == 1 or x == 2:
        return 1
    else:
        return fib(x-1) + fib(x-2)

print(fib(100))