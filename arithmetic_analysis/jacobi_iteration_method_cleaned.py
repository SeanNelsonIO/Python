
from __future__ import annotations

import numpy as np



def jacobi_iteration_method(
    coefficient_matrix: np.ndarray,
    constant_matrix: np.ndarray,
    init_val: list,
    iterations: int,
) -> list[float]:
    

    rows1, cols1 = coefficient_matrix.shape
    rows2, cols2 = constant_matrix.shape

    if rows1 != cols1:
        raise ValueError(
            f"Coefficient matrix dimensions must be nxn but received {rows1}x{cols1}"
        )

    if cols2 != 1:
        raise ValueError(f"Constant matrix must be nx1 but received {rows2}x{cols2}")

    if rows1 != rows2:
        raise ValueError(
            f"""Coefficient and constant matrices dimensions must be nxn and nx1 but
            received {rows1}x{cols1} and {rows2}x{cols2}"""
        )

    if len(init_val) != rows1:
        raise ValueError(
            f"""Number of initial values must be equal to number of rows in coefficient
            matrix but received {len(init_val)} and {rows1}"""
        )

    if iterations <= 0:
        raise ValueError("Iterations must be at least 1")

    table = np.concatenate((coefficient_matrix, constant_matrix), axis=1)

    rows, cols = table.shape

    strictly_diagonally_dominant(table)

    
    for i in range(iterations):
        new_val = []
        for row in range(rows):
            temp = 0
            for col in range(cols):
                if col == row:
                    denom = table[row][col]
                elif col == cols - 1:
                    val = table[row][col]
                else:
                    temp += (-1) * table[row][col] * init_val[col]
            temp = (temp + val) / denom
            new_val.append(temp)
        init_val = new_val

    return [float(i) for i in new_val]



def strictly_diagonally_dominant(table: np.ndarray) -> bool:
    

    rows, cols = table.shape

    is_diagonally_dominant = True

    for i in range(0, rows):
        sum = 0
        for j in range(0, cols - 1):
            if i == j:
                continue
            else:
                sum += table[i][j]

        if table[i][i] <= sum:
            raise ValueError("Coefficient matrix is not strictly diagonally dominant")

    return is_diagonally_dominant



if __name__ == "__main__":
    import doctest

    doctest.testmod()
