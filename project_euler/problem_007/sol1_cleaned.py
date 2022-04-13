

from math import sqrt


def is_prime(num: int) -> bool:
    

    if num == 2:
        return True
    elif num % 2 == 0:
        return False
    else:
        sq = int(sqrt(num)) + 1
        for i in range(3, sq, 2):
            if num % i == 0:
                return False
    return True


def solution(nth: int = 10001) -> int:
    

    count = 0
    number = 1
    while count != nth and number < 3:
        number += 1
        if is_prime(number):
            count += 1
    while count != nth:
        number += 2
        if is_prime(number):
            count += 1
    return number


if __name__ == "__main__":
    print(f"{solution() = }")
