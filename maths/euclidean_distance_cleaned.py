from __future__ import annotations

from typing import Iterable, Union

import numpy as np

Vector = Union[Iterable[float], Iterable[int], np.ndarray]
VectorOut = Union[np.float64, int, float]


def euclidean_distance(vector_1: Vector, vector_2: Vector) -> VectorOut:
    
    return np.sqrt(np.sum((np.asarray(vector_1) - np.asarray(vector_2)) ** 2))


def euclidean_distance_no_np(vector_1: Vector, vector_2: Vector) -> VectorOut:
    
    return sum((v1 - v2) ** 2 for v1, v2 in zip(vector_1, vector_2)) ** (1 / 2)


if __name__ == "__main__":

    def benchmark() -> None:
        
        from timeit import timeit

        print("Without Numpy")
        print(
            timeit(
                "euclidean_distance_no_np([1, 2, 3], [4, 5, 6])",
                number=10000,
                globals=globals(),
            )
        )
        print("With Numpy")
        print(
            timeit(
                "euclidean_distance([1, 2, 3], [4, 5, 6])",
                number=10000,
                globals=globals(),
            )
        )

    benchmark()
