import math
from typing import Generator


def slow_primes(max: int) -> Generator[int, None, None]:
    
    numbers: Generator = (i for i in range(1, (max + 1)))
    for i in (n for n in numbers if n > 1):
        for j in range(2, i):
            if (i % j) == 0:
                break
        else:
            yield i


def primes(max: int) -> Generator[int, None, None]:
    
    numbers: Generator = (i for i in range(1, (max + 1)))
    for i in (n for n in numbers if n > 1):
        
        bound = int(math.sqrt(i)) + 1
        for j in range(2, bound):
            if (i % j) == 0:
                break
        else:
            yield i


def fast_primes(max: int) -> Generator[int, None, None]:
    
    numbers: Generator = (i for i in range(1, (max + 1), 2))
    
    if max > 2:
        yield 2  
    for i in (n for n in numbers if n > 1):
        bound = int(math.sqrt(i)) + 1
        for j in range(3, bound, 2):
            
            if (i % j) == 0:
                break
        else:
            yield i


if __name__ == "__main__":
    number = int(input("Calculate primes up to:\n>> ").strip())
    for ret in primes(number):
        print(ret)

    
    from timeit import timeit

    print(
        timeit(
            "slow_primes(1_000_000_000_000)",
            setup="from __main__ import slow_primes",
            number=1_000_000,
        )
    )
    print(
        timeit(
            "primes(1_000_000_000_000)",
            setup="from __main__ import primes",
            number=1_000_000,
        )
    )
    print(
        timeit(
            "fast_primes(1_000_000_000_000)",
            setup="from __main__ import fast_primes",
            number=1_000_000,
        )
    )
