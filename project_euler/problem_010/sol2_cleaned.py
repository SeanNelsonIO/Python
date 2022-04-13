
import math
from itertools import takewhile
from typing import Iterator


def is_prime(number: int) -> bool:
    

    if number % 2 == 0 and number > 2:
        return False
    return all(number % i for i in range(3, int(math.sqrt(number)) + 1, 2))


def prime_generator() -> Iterator[int]:
    

    num = 2
    while True:
        if is_prime(num):
            yield num
        num += 1


def solution(n: int = 2000000) -> int:
    

    return sum(takewhile(lambda x: x < n, prime_generator()))


if __name__ == "__main__":
    print(f"{solution() = }")
