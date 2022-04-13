


import numpy as np


def retroactive_resolution(coefficients: np.matrix, vector: np.ndarray) -> np.ndarray:
    

    rows, columns = np.shape(coefficients)

    x = np.zeros((rows, 1), dtype=float)
    for row in reversed(range(rows)):
        sum = 0
        for col in range(row + 1, columns):
            sum += coefficients[row, col] * x[col]

        x[row, 0] = (vector[row] - sum) / coefficients[row, row]

    return x


def gaussian_elimination(coefficients: np.matrix, vector: np.ndarray) -> np.ndarray:
    
    
    rows, columns = np.shape(coefficients)
    if rows != columns:
        return np.array((), dtype=float)

    
    augmented_mat = np.concatenate((coefficients, vector), axis=1)
    augmented_mat = augmented_mat.astype("float64")

    
    for row in range(rows - 1):
        pivot = augmented_mat[row, row]
        for col in range(row + 1, columns):
            factor = augmented_mat[col, row] / pivot
            augmented_mat[col, :] -= factor * augmented_mat[row, :]

    x = retroactive_resolution(
        augmented_mat[:, 0:columns], augmented_mat[:, columns : columns + 1]
    )

    return x


if __name__ == "__main__":
    import doctest

    doctest.testmod()
