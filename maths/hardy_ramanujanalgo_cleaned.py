


import math


def exactPrimeFactorCount(n):
    
    count = 0
    if n % 2 == 0:
        count += 1
        while n % 2 == 0:
            n = int(n / 2)
    
    

    i = 3

    while i <= int(math.sqrt(n)):
        if n % i == 0:
            count += 1
            while n % i == 0:
                n = int(n / i)
        i = i + 2

    
    

    if n > 2:
        count += 1
    return count


if __name__ == "__main__":
    n = 51242183
    print(f"The number of distinct prime factors is/are {exactPrimeFactorCount(n)}")
    print(f"The value of log(log(n)) is {math.log(math.log(n)):.4f}")

    """
    The number of distinct prime factors is/are 3
    The value of log(log(n)) is 2.8765
    """
