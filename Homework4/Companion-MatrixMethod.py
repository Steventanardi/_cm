import numpy as np

def roots_companion(c):
    """
    Return all roots (complex) of polynomial with coefficients c[0..n]
    where c[k] is the coefficient of x^k (ascending order).
    Uses eigenvalues of the companion matrix of the monic polynomial.
    """
    # remove leading zeros at the high-degree end
    i = len(c) - 1
    while i > 0 and abs(c[i]) == 0:
        i -= 1
    c = c[:i+1]
    n = len(c) - 1
    if n <= 0:
        raise ValueError("Polynomial degree must be >= 1.")
    # normalize to monic: divide all by leading coeff
    c = np.array(c, dtype=np.complex128)
    c = c / c[-1]

    # Companion matrix (size n x n)
    # [ 0  0 ... 0  -c0 ]
    # [ 1  0 ... 0  -c1 ]
    # [ 0  1 ... 0  -c2 ]
    # ...
    # [ 0  0 ... 1  -c_{n-1} ]
    A = np.zeros((n, n), dtype=np.complex128)
    A[1:, :-1] = np.eye(n-1)
    A[:, -1] = -c[:-1]

    vals = np.linalg.eigvals(A)
    return vals  # complex ndarray
