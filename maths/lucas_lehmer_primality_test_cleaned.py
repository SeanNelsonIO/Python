




def lucas_lehmer_test(p: int) -> bool:
    

    if p < 2:
        raise ValueError("p should not be less than 2!")
    elif p == 2:
        return True

    s = 4
    M = (1 << p) - 1
    for i in range(p - 2):
        s = ((s * s) - 2) % M
    return s == 0


if __name__ == "__main__":
    print(lucas_lehmer_test(7))
    print(lucas_lehmer_test(11))
