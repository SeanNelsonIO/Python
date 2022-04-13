


def factorial(number: int) -> int:
    
    if number != int(number):
        raise ValueError("factorial() only accepts integral values")
    if number < 0:
        raise ValueError("factorial() not defined for negative values")
    value = 1
    for i in range(1, number + 1):
        value *= i
    return value


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    n = int(input("Enter a positive integer: ").strip() or 0)
    print(f"factorial{n} is {factorial(n)}")
