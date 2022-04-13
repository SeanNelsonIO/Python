


def climb_stairs(n: int) -> int:
    
    assert (
        isinstance(n, int) and n > 0
    ), f"n needs to be positive integer, your input {n}"
    if n == 1:
        return 1
    dp = [0] * (n + 1)
    dp[0], dp[1] = (1, 1)
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]


if __name__ == "__main__":
    import doctest

    doctest.testmod()
