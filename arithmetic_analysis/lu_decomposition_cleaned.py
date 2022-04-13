
from __future__ import annotations

import numpy as np


def lower_upper_decomposition(table: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    
    
    
    rows, columns = np.shape(table)
    if rows != columns:
        raise ValueError(
            f"'table' has to be of square shaped array but got a {rows}x{columns} "
            + f"array:\n{table}"
        )
    lower = np.zeros((rows, columns))
    upper = np.zeros((rows, columns))
    for i in range(columns):
        for j in range(i):
            total = 0
            for k in range(j):
                total += lower[i][k] * upper[k][j]
            lower[i][j] = (table[i][j] - total) / upper[j][j]
        lower[i][i] = 1
        for j in range(i, columns):
            total = 0
            for k in range(i):
                total += lower[i][k] * upper[k][j]
            upper[i][j] = table[i][j] - total
    return lower, upper


if __name__ == "__main__":
    import doctest

    doctest.testmod()
