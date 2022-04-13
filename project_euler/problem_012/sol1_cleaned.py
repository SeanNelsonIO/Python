


def count_divisors(n):
    nDivisors = 1
    i = 2
    while i * i <= n:
        multiplicity = 0
        while n % i == 0:
            n //= i
            multiplicity += 1
        nDivisors *= multiplicity + 1
        i += 1
    if n > 1:
        nDivisors *= 2
    return nDivisors


def solution():
    
    tNum = 1
    i = 1

    while True:
        i += 1
        tNum += i

        if count_divisors(tNum) > 500:
            break

    return tNum


if __name__ == "__main__":
    print(solution())
