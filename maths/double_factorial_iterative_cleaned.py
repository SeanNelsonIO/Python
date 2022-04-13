def double_factorial(num: int) -> int:
    
    if not isinstance(num, int):
        raise ValueError("double_factorial() only accepts integral values")
    if num < 0:
        raise ValueError("double_factorial() not defined for negative values")
    value = 1
    for i in range(num, 0, -2):
        value *= i
    return value


if __name__ == "__main__":
    import doctest

    doctest.testmod()
