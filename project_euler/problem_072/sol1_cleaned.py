


def solution(limit: int = 1_000_000) -> int:
    

    phi = [i - 1 for i in range(limit + 1)]

    for i in range(2, limit + 1):
        if phi[i] == i - 1:
            for j in range(2 * i, limit + 1, i):
                phi[j] -= phi[j] // i

    return sum(phi[2 : limit + 1])


if __name__ == "__main__":
    print(solution())
