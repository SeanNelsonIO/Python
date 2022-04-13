

from math import floor, sqrt


def continuous_fraction_period(n: int) -> int:
    
    numerator = 0.0
    denominator = 1.0
    ROOT = int(sqrt(n))
    integer_part = ROOT
    period = 0
    while integer_part != 2 * ROOT:
        numerator = denominator * integer_part - numerator
        denominator = (n - numerator**2) / denominator
        integer_part = int((ROOT + numerator) / denominator)
        period += 1
    return period


def solution(n: int = 10000) -> int:
    
    count_odd_periods = 0
    for i in range(2, n + 1):
        sr = sqrt(i)
        if sr - floor(sr) != 0:
            if continuous_fraction_period(i) % 2 == 1:
                count_odd_periods += 1
    return count_odd_periods


if __name__ == "__main__":
    print(f"{solution(int(input().strip()))}")
