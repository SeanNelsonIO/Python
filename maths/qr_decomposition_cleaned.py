import numpy as np


def qr_householder(A):
    
    m, n = A.shape
    t = min(m, n)
    Q = np.eye(m)
    R = A.copy()

    for k in range(t - 1):
        
        x = R[k:, [k]]
        
        e1 = np.zeros_like(x)
        e1[0] = 1.0
        
        alpha = np.linalg.norm(x)
        
        v = x + np.sign(x[0]) * alpha * e1
        v /= np.linalg.norm(v)

        
        Q_k = np.eye(m - k) - 2.0 * v @ v.T
        
        Q_k = np.block([[np.eye(k), np.zeros((k, m - k))], [np.zeros((m - k, k)), Q_k]])

        Q = Q @ Q_k.T
        R = Q_k @ R

    return Q, R


if __name__ == "__main__":
    import doctest

    doctest.testmod()
