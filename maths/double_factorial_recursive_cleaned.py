def double_factorial(n: int) -> int:
    
    if not isinstance(n, int):
        raise ValueError("double_factorial() only accepts integral values")
    if n < 0:
        raise ValueError("double_factorial() not defined for negative values")
    return 1 if n <= 1 else n * double_factorial(n - 2)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
