import cmath
from math import tau  # 2*pi

def poly_eval(c, x):
    """Horner evaluation for coefficients c[0..n] (ascending)."""
    acc = 0j
    for coeff in reversed(c):
        acc = acc * x + coeff
    return acc

def roots_durand_kerner(c, tol=1e-12, max_iter=200):
    """
    Return all roots (complex) of polynomial with coefficients c[0..n],
    c[k] = coeff of x^k (ascending). Pure-Python, no NumPy.
    """
    # strip highest leading zeros
    i = len(c) - 1
    while i > 0 and abs(c[i]) == 0:
        i -= 1
    c = c[:i+1]
    n = len(c) - 1
    if n <= 0:
        raise ValueError("Polynomial degree must be >= 1.")

    # scale to monic for better conditioning
    lead = c[-1]
    c = [ck / lead for ck in c]

    # initial guesses: points on a circle
    R = 1 + max(abs(ck) for ck in c[:-1])  # simple bound
    roots = [R * cmath.exp(1j * tau * k / n) for k in range(n)]

    for _ in range(max_iter):
        moved = 0.0
        for i in range(n):
            xi = roots[i]
            denom = 1+0j
            for j in range(n):
                if i != j:
                    denom *= (xi - roots[j])
            if denom == 0:
                # small random nudge if two guesses collide
                xi += 1e-12 + 1e-12j
                denom = 1e-12 + 1e-12j
            delta = poly_eval(c, xi) / denom
            roots[i] = xi - delta
            moved = max(moved, abs(delta))
        if moved < tol:
            break
    return roots
