


def is_prime(number: int) -> bool:
    

    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True


def solution(nth: int = 10001) -> int:
    

    try:
        nth = int(nth)
    except (TypeError, ValueError):
        raise TypeError("Parameter nth must be int or castable to int.") from None
    if nth <= 0:
        raise ValueError("Parameter nth must be greater than or equal to one.")
    primes: list[int] = []
    num = 2
    while len(primes) < nth:
        if is_prime(num):
            primes.append(num)
            num += 1
        else:
            num += 1
    return primes[len(primes) - 1]


if __name__ == "__main__":
    print(f"{solution() = }")
