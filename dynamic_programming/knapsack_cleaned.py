


def MF_knapsack(i, wt, val, j):
    
    global F  
    if F[i][j] < 0:
        if j < wt[i - 1]:
            val = MF_knapsack(i - 1, wt, val, j)
        else:
            val = max(
                MF_knapsack(i - 1, wt, val, j),
                MF_knapsack(i - 1, wt, val, j - wt[i - 1]) + val[i - 1],
            )
        F[i][j] = val
    return F[i][j]


def knapsack(W, wt, val, n):
    dp = [[0 for i in range(W + 1)] for j in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(1, W + 1):
            if wt[i - 1] <= w:
                dp[i][w] = max(val[i - 1] + dp[i - 1][w - wt[i - 1]], dp[i - 1][w])
            else:
                dp[i][w] = dp[i - 1][w]

    return dp[n][W], dp


def knapsack_with_example_solution(W: int, wt: list, val: list):
    
    if not (isinstance(wt, (list, tuple)) and isinstance(val, (list, tuple))):
        raise ValueError(
            "Both the weights and values vectors must be either lists or tuples"
        )

    num_items = len(wt)
    if num_items != len(val):
        raise ValueError(
            "The number of weights must be the "
            "same as the number of values.\nBut "
            f"got {num_items} weights and {len(val)} values"
        )
    for i in range(num_items):
        if not isinstance(wt[i], int):
            raise TypeError(
                "All weights must be integers but "
                f"got weight of type {type(wt[i])} at index {i}"
            )

    optimal_val, dp_table = knapsack(W, wt, val, num_items)
    example_optional_set: set = set()
    _construct_solution(dp_table, wt, num_items, W, example_optional_set)

    return optimal_val, example_optional_set


def _construct_solution(dp: list, wt: list, i: int, j: int, optimal_set: set):
    
    
    
    
    if i > 0 and j > 0:
        if dp[i - 1][j] == dp[i][j]:
            _construct_solution(dp, wt, i - 1, j, optimal_set)
        else:
            optimal_set.add(i)
            _construct_solution(dp, wt, i - 1, j - wt[i - 1], optimal_set)


if __name__ == "__main__":
    
    val = [3, 2, 4, 4]
    wt = [4, 3, 2, 3]
    n = 4
    w = 6
    F = [[0] * (w + 1)] + [[0] + [-1 for i in range(w + 1)] for j in range(n + 1)]
    optimal_solution, _ = knapsack(w, wt, val, n)
    print(optimal_solution)
    print(MF_knapsack(n, wt, val, w))  

    
    
    optimal_solution, optimal_subset = knapsack_with_example_solution(w, wt, val)
    assert optimal_solution == 8
    assert optimal_subset == {3, 4}
    print("optimal_value = ", optimal_solution)
    print("An optimal subset corresponding to the optimal value", optimal_subset)
