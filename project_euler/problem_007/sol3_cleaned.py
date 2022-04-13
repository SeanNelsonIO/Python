
import itertools
import math


def is_prime(number: int) -> bool:
    

    if number % 2 == 0 and number > 2:
        return False
    return all(number % i for i in range(3, int(math.sqrt(number)) + 1, 2))


def prime_generator():
    

    num = 2
    while True:
        if is_prime(num):
            yield num
        num += 1


def solution(nth: int = 10001) -> int:
    
    return next(itertools.islice(prime_generator(), nth - 1, nth))


if __name__ == "__main__":
    print(f"{solution() = }")
