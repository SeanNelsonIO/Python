
import math


def is_prime(num: int) -> bool:
    

    if num <= 1:
        raise ValueError("Parameter num must be greater than or equal to two.")
    if num == 2:
        return True
    elif num % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(num)) + 1, 2):
        if num % i == 0:
            return False
    return True


def solution(n: int = 600851475143) -> int:
    

    try:
        n = int(n)
    except (TypeError, ValueError):
        raise TypeError("Parameter n must be int or castable to int.")
    if n <= 0:
        raise ValueError("Parameter n must be greater than or equal to one.")
    max_number = 0
    if is_prime(n):
        return n
    while n % 2 == 0:
        n //= 2
    if is_prime(n):
        return n
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            if is_prime(n // i):
                max_number = n // i
                break
            elif is_prime(i):
                max_number = i
    return max_number


if __name__ == "__main__":
    print(f"{solution() = }")
