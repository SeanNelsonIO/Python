

from math import sqrt


def is_prime(n: int) -> bool:
    

    if 1 < n < 4:
        return True
    elif n < 2 or not n % 2:
        return False
    return not any(not n % i for i in range(3, int(sqrt(n) + 1), 2))


def solution(n: int = 2000000) -> int:
    

    return sum(num for num in range(3, n, 2) if is_prime(num)) + 2 if n > 2 else 0


if __name__ == "__main__":
    print(f"{solution() = }")
