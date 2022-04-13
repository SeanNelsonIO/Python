


DIGITS_SQUARED = [digit**2 for digit in range(10)]


def next_number(number: int) -> int:
    
    sum_of_digits_squared = 0
    while number:
        sum_of_digits_squared += DIGITS_SQUARED[number % 10]
        number //= 10

    return sum_of_digits_squared


CHAINS = {1: True, 58: False}


def chain(number: int) -> bool:
    
    if number in CHAINS:
        return CHAINS[number]

    number_chain = chain(next_number(number))
    CHAINS[number] = number_chain

    return number_chain


def solution(number: int = 10000000) -> int:
    
    return sum(1 for i in range(1, number) if not chain(i))


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    print(f"{solution() = }")
