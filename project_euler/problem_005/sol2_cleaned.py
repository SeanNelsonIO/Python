


def gcd(x: int, y: int) -> int:
    

    return x if y == 0 else gcd(y, x % y)


def lcm(x: int, y: int) -> int:
    

    return (x * y) // gcd(x, y)


def solution(n: int = 20) -> int:
    

    g = 1
    for i in range(1, n + 1):
        g = lcm(g, i)
    return g


if __name__ == "__main__":
    print(f"{solution() = }")
