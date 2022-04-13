


def solution(limit=28123):
    
    sumDivs = [1] * (limit + 1)

    for i in range(2, int(limit**0.5) + 1):
        sumDivs[i * i] += i
        for k in range(i + 1, limit // i + 1):
            sumDivs[k * i] += k + i

    abundants = set()
    res = 0

    for n in range(1, limit + 1):
        if sumDivs[n] > n:
            abundants.add(n)

        if not any((n - a in abundants) for a in abundants):
            res += n

    return res


if __name__ == "__main__":
    print(solution())
