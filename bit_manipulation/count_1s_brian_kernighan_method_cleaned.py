def get_1s_count(number: int) -> int:
    
    if number < 0:
        raise ValueError("the value of input must be positive")
    elif isinstance(number, float):
        raise TypeError("Input value must be an 'int' type")
    count = 0
    while number:
        
        
        
        number &= number - 1
        count += 1
    return count


if __name__ == "__main__":
    import doctest

    doctest.testmod()
