


from __future__ import annotations

import matplotlib.pyplot as plt  
import numpy


VECTOR_1 = numpy.array([0, 0])
VECTOR_2 = numpy.array([0.5, 0.8660254])
VECTOR_3 = numpy.array([1, 0])
INITIAL_VECTORS = [VECTOR_1, VECTOR_2, VECTOR_3, VECTOR_1]





def iterate(initial_vectors: list[numpy.ndarray], steps: int) -> list[numpy.ndarray]:
    
    vectors = initial_vectors
    for i in range(steps):
        vectors = iteration_step(vectors)
    return vectors


def iteration_step(vectors: list[numpy.ndarray]) -> list[numpy.ndarray]:
    
    new_vectors = []
    for i, start_vector in enumerate(vectors[:-1]):
        end_vector = vectors[i + 1]
        new_vectors.append(start_vector)
        difference_vector = end_vector - start_vector
        new_vectors.append(start_vector + difference_vector / 3)
        new_vectors.append(
            start_vector + difference_vector / 3 + rotate(difference_vector / 3, 60)
        )
        new_vectors.append(start_vector + difference_vector * 2 / 3)
    new_vectors.append(vectors[-1])
    return new_vectors


def rotate(vector: numpy.ndarray, angle_in_degrees: float) -> numpy.ndarray:
    
    theta = numpy.radians(angle_in_degrees)
    c, s = numpy.cos(theta), numpy.sin(theta)
    rotation_matrix = numpy.array(((c, -s), (s, c)))
    return numpy.dot(rotation_matrix, vector)


def plot(vectors: list[numpy.ndarray]) -> None:
    
    
    axes = plt.gca()
    axes.set_aspect("equal")

    
    
    
    x_coordinates, y_coordinates = zip(*vectors)
    plt.plot(x_coordinates, y_coordinates)
    plt.show()


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    processed_vectors = iterate(INITIAL_VECTORS, 5)
    plot(processed_vectors)
