import math


def fx(x: float, a: float) -> float:
    return math.pow(x, 2) - a


def fx_derivative(x: float) -> float:
    return 2 * x


def get_initial_point(a: float) -> float:
    start = 2.0

    while start <= a:
        start = math.pow(start, 2)

    return start


def square_root_iterative(
    a: float, max_iter: int = 9999, tolerance: float = 0.00000000000001
) -> float:
    

    if a < 0:
        raise ValueError("math domain error")

    value = get_initial_point(a)

    for i in range(max_iter):
        prev_value = value
        value = value - fx(value, a) / fx_derivative(value)
        if abs(prev_value - value) < tolerance:
            return value

    return value


if __name__ == "__main__":
    from doctest import testmod

    testmod()
