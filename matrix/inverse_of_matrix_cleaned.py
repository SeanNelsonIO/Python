from __future__ import annotations

from decimal import Decimal


def inverse_of_matrix(matrix: list[list[float]]) -> list[list[float]]:
    

    D = Decimal  
    
    determinant = D(matrix[0][0]) * D(matrix[1][1]) - D(matrix[1][0]) * D(matrix[0][1])
    if determinant == 0:
        raise ValueError("This matrix has no inverse.")
    
    swapped_matrix = [[0.0, 0.0], [0.0, 0.0]]
    swapped_matrix[0][0], swapped_matrix[1][1] = matrix[1][1], matrix[0][0]
    swapped_matrix[1][0], swapped_matrix[0][1] = -matrix[1][0], -matrix[0][1]
    
    return [[float(D(n) / determinant) or 0.0 for n in row] for row in swapped_matrix]
