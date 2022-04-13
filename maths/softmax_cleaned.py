

import numpy as np


def softmax(vector):
    

    
    
    exponentVector = np.exp(vector)

    
    sumOfExponents = np.sum(exponentVector)

    
    softmax_vector = exponentVector / sumOfExponents

    return softmax_vector


if __name__ == "__main__":
    print(softmax((0,)))
