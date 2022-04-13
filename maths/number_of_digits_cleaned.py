import math
from timeit import timeit


def num_digits(n: int) -> int:
    
    digits = 0
    n = abs(n)
    while True:
        n = n // 10
        digits += 1
        if n == 0:
            break
    return digits


def num_digits_fast(n: int) -> int:
    
    return 1 if n == 0 else math.floor(math.log(abs(n), 10) + 1)


def num_digits_faster(n: int) -> int:
    
    return len(str(abs(n)))


def benchmark() -> None:
    
    print("\nFor small_num = ", small_num, ":")
    print(
        "> num_digits()",
        "\t\tans =",
        num_digits(small_num),
        "\ttime =",
        timeit("z.num_digits(z.small_num)", setup="import __main__ as z"),
        "seconds",
    )
    print(
        "> num_digits_fast()",
        "\tans =",
        num_digits_fast(small_num),
        "\ttime =",
        timeit("z.num_digits_fast(z.small_num)", setup="import __main__ as z"),
        "seconds",
    )
    print(
        "> num_digits_faster()",
        "\tans =",
        num_digits_faster(small_num),
        "\ttime =",
        timeit("z.num_digits_faster(z.small_num)", setup="import __main__ as z"),
        "seconds",
    )

    print("\nFor medium_num = ", medium_num, ":")
    print(
        "> num_digits()",
        "\t\tans =",
        num_digits(medium_num),
        "\ttime =",
        timeit("z.num_digits(z.medium_num)", setup="import __main__ as z"),
        "seconds",
    )
    print(
        "> num_digits_fast()",
        "\tans =",
        num_digits_fast(medium_num),
        "\ttime =",
        timeit("z.num_digits_fast(z.medium_num)", setup="import __main__ as z"),
        "seconds",
    )
    print(
        "> num_digits_faster()",
        "\tans =",
        num_digits_faster(medium_num),
        "\ttime =",
        timeit("z.num_digits_faster(z.medium_num)", setup="import __main__ as z"),
        "seconds",
    )

    print("\nFor large_num = ", large_num, ":")
    print(
        "> num_digits()",
        "\t\tans =",
        num_digits(large_num),
        "\ttime =",
        timeit("z.num_digits(z.large_num)", setup="import __main__ as z"),
        "seconds",
    )
    print(
        "> num_digits_fast()",
        "\tans =",
        num_digits_fast(large_num),
        "\ttime =",
        timeit("z.num_digits_fast(z.large_num)", setup="import __main__ as z"),
        "seconds",
    )
    print(
        "> num_digits_faster()",
        "\tans =",
        num_digits_faster(large_num),
        "\ttime =",
        timeit("z.num_digits_faster(z.large_num)", setup="import __main__ as z"),
        "seconds",
    )


if __name__ == "__main__":
    small_num = 262144
    medium_num = 1125899906842624
    large_num = 1267650600228229401496703205376
    benchmark()
    import doctest

    doctest.testmod()
