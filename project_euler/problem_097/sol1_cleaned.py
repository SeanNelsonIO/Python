


def solution(n: int = 10) -> str:
    
    if not isinstance(n, int) or n < 0:
        raise ValueError("Invalid input")
    MODULUS = 10**n
    NUMBER = 28433 * (pow(2, 7830457, MODULUS)) + 1
    return str(NUMBER % MODULUS)


if __name__ == "__main__":
    from doctest import testmod

    testmod()
    print(f"{solution(10) = }")
