

import numpy as np


def sigmoid(vector: np.array) -> np.array:
    
    return 1 / (1 + np.exp(-vector))


if __name__ == "__main__":
    import doctest

    doctest.testmod()
