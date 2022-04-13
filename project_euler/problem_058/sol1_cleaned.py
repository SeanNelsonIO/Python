
from math import isqrt


def is_prime(number: int) -> int:
    
    if number == 1:
        return 0

    if number % 2 == 0 and number > 2:
        return 0

    for i in range(3, isqrt(number) + 1, 2):
        if number % i == 0:
            return 0
    return 1


def solution(ratio: float = 0.1) -> int:
    

    j = 3
    primes = 3

    while primes / (2 * j - 1) >= ratio:
        for i in range(j * j + j + 1, (j + 2) * (j + 2), j + 1):
            primes += is_prime(i)
        j += 2
    return j


if __name__ == "__main__":
    import doctest

    doctest.testmod()
