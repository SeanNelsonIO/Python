

from math import sqrt
from time import time


def time_func(func, *args, **kwargs):
    
    start = time()
    output = func(*args, **kwargs)
    end = time()
    if int(end - start) > 0:
        print(f"{func.__name__} runtime: {(end - start):0.4f} s")
    else:
        print(f"{func.__name__} runtime: {(end - start) * 1000:0.4f} ms")
    return output


def fib_iterative(n: int) -> list[int]:
    
    if n < 0:
        raise Exception("n is negative")
    if n == 0:
        return [0]
    fib = [0, 1]
    for _ in range(n - 1):
        fib.append(fib[-1] + fib[-2])
    return fib


def fib_recursive(n: int) -> list[int]:
    

    def fib_recursive_term(i: int) -> int:
        
        if i < 0:
            raise Exception("n is negative")
        if i < 2:
            return i
        return fib_recursive_term(i - 1) + fib_recursive_term(i - 2)

    if n < 0:
        raise Exception("n is negative")
    return [fib_recursive_term(i) for i in range(n + 1)]


def fib_memoization(n: int) -> list[int]:
    
    if n < 0:
        raise Exception("n is negative")
    
    
    cache: dict[int, int] = {0: 0, 1: 1, 2: 1}  

    def rec_fn_memoized(num: int) -> int:
        if num in cache:
            return cache[num]

        value = rec_fn_memoized(num - 1) + rec_fn_memoized(num - 2)
        cache[num] = value
        return value

    return [rec_fn_memoized(i) for i in range(n + 1)]


def fib_binet(n: int) -> list[int]:
    
    if n < 0:
        raise Exception("n is negative")
    if n >= 1475:
        raise Exception("n is too large")
    sqrt_5 = sqrt(5)
    phi = (1 + sqrt_5) / 2
    return [round(phi**i / sqrt_5) for i in range(n + 1)]


if __name__ == "__main__":
    num = 20
    time_func(fib_iterative, num)
    time_func(fib_recursive, num)
    time_func(fib_memoization, num)
    time_func(fib_binet, num)
