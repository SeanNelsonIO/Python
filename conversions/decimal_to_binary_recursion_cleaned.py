def binary_recursive(decimal: int) -> str:
    
    decimal = int(decimal)
    if decimal in (0, 1):  
        return str(decimal)
    div, mod = divmod(decimal, 2)
    return binary_recursive(div) + str(mod)


def main(number: str) -> str:
    
    number = str(number).strip()
    if not number:
        raise ValueError("No input value was provided")
    negative = "-" if number.startswith("-") else ""
    number = number.lstrip("-")
    if not number.isnumeric():
        raise ValueError("Input value is not an integer")
    return f"{negative}0b{binary_recursive(int(number))}"


if __name__ == "__main__":
    from doctest import testmod

    testmod()
