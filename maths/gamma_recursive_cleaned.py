
from math import pi, sqrt


def gamma(num: float) -> float:
    
    if num <= 0:
        raise ValueError("math domain error")
    if num > 171.5:
        raise OverflowError("math range error")
    elif num - int(num) not in (0, 0.5):
        raise NotImplementedError("num must be an integer or a half-integer")
    elif num == 0.5:
        return sqrt(pi)
    else:
        return 1.0 if num == 1 else (num - 1) * gamma(num - 1)


def test_gamma() -> None:
    
    assert gamma(0.5) == sqrt(pi)
    assert gamma(1) == 1.0
    assert gamma(2) == 1.0


if __name__ == "__main__":
    from doctest import testmod

    testmod()
    num = 1.0
    while num:
        num = float(input("Gamma of: "))
        print(f"gamma({num}) = {gamma(num)}")
        print("\nEnter 0 to exit...")
