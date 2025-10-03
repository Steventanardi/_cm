import cmath

def cubic_roots(a, b, c, d):
    """Solve ax^3 + bx^2 + cx + d = 0 and return three roots (real or complex)."""
    if a == 0:
        raise ValueError("Coefficient 'a' cannot be zero for a cubic equation.")
    
    p = (3*a*c - b**2) / (3*a**2)
    q = (2*b**3 - 9*a*b*c + 27*a**2*d) / (27*a**3)

    discriminant = (q/2)**2 + (p/3)**3

    def cbrt(z):
        return z**(1/3) if z.imag >= 0 else -(-z)**(1/3)

    C = cmath.exp(cmath.log(-q/2 + cmath.sqrt(discriminant))/3)

    omega = complex(-0.5, cmath.sqrt(3)/2)  # e^(2πi/3)

    roots = []
    for k in range(3):
        y = C * (omega**k) + (p/(3*C)) * (omega**(-k))
        x = y - b/(3*a)
        roots.append(x)

    return roots


if __name__ == "__main__":
    roots = cubic_roots(1, -6, 11, -6)
    print("Roots of x^3 - 6x^2 + 11x - 6:", roots)

    roots = cubic_roots(1, 0, 1, 1)
    print("Roots of x^3 + x + 1:", roots)
