import numpy as np


def power_iteration(
    input_matrix: np.ndarray,
    vector: np.ndarray,
    error_tol: float = 1e-12,
    max_iterations: int = 100,
) -> tuple[float, np.ndarray]:
    

    
    assert np.shape(input_matrix)[0] == np.shape(input_matrix)[1]
    
    assert np.shape(input_matrix)[0] == np.shape(vector)[0]
    
    assert np.iscomplexobj(input_matrix) == np.iscomplexobj(vector)
    is_complex = np.iscomplexobj(input_matrix)
    if is_complex:
        
        assert np.array_equal(input_matrix, input_matrix.conj().T)

    
    

    convergence = False
    lamda_previous = 0
    iterations = 0
    error = 1e12

    while not convergence:
        
        w = np.dot(input_matrix, vector)
        
        vector = w / np.linalg.norm(w)
        
        
        vectorH = vector.conj().T if is_complex else vector.T
        lamda = np.dot(vectorH, np.dot(input_matrix, vector))

        
        error = np.abs(lamda - lamda_previous) / lamda
        iterations += 1

        if error <= error_tol or iterations >= max_iterations:
            convergence = True

        lamda_previous = lamda

    if is_complex:
        lamda = np.real(lamda)

    return lamda, vector


def test_power_iteration() -> None:
    
    real_input_matrix = np.array([[41, 4, 20], [4, 26, 30], [20, 30, 50]])
    real_vector = np.array([41, 4, 20])
    complex_input_matrix = real_input_matrix.astype(np.complex128)
    imag_matrix = np.triu(1j * complex_input_matrix, 1)
    complex_input_matrix += imag_matrix
    complex_input_matrix += -1 * imag_matrix.T
    complex_vector = np.array([41, 4, 20]).astype(np.complex128)

    for problem_type in ["real", "complex"]:
        if problem_type == "real":
            input_matrix = real_input_matrix
            vector = real_vector
        elif problem_type == "complex":
            input_matrix = complex_input_matrix
            vector = complex_vector

        
        eigen_value, eigen_vector = power_iteration(input_matrix, vector)

        

        
        
        eigen_values, eigen_vectors = np.linalg.eigh(input_matrix)
        
        eigen_value_max = eigen_values[-1]
        
        eigen_vector_max = eigen_vectors[:, -1]

        
        assert np.abs(eigen_value - eigen_value_max) <= 1e-6
        
        
        assert np.linalg.norm(np.abs(eigen_vector) - np.abs(eigen_vector_max)) <= 1e-6


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    test_power_iteration()
