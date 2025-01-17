def actual_power(a: int, b: int):
    
    if b == 0:
        return 1
    if (b % 2) == 0:
        return actual_power(a, int(b / 2)) * actual_power(a, int(b / 2))
    else:
        return a * actual_power(a, int(b / 2)) * actual_power(a, int(b / 2))


def power(a: int, b: int) -> float:
    
    if b < 0:
        return 1 / actual_power(a, b)
    return actual_power(a, b)


if __name__ == "__main__":
    print(power(-2, -3))
