def reverse_letters(input_str: str) -> str:
    
    return " ".join([word[::-1] for word in input_str.split()])


if __name__ == "__main__":
    import doctest

    doctest.testmod()
