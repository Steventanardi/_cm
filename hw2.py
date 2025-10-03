import cmath

def quadratic_roots(a, b, c):
    """Solve ax^2 + bx + c = 0 and return two roots (possibly complex)."""
    if a == 0:
        raise ValueError("Coefficient 'a' cannot be zero for a quadratic equation.")

    discriminant = b**2 - 4*a*c
    root1 = (-b + cmath.sqrt(discriminant)) / (2*a)
    root2 = (-b - cmath.sqrt(discriminant)) / (2*a)

    # Verify results
    def f(x):
        return a*x**2 + b*x + c

    print(f"Root 1: {root1}, f(root1) ≈ {f(root1)}")
    print(f"Root 2: {root2}, f(root2) ≈ {f(root2)}")

    assert cmath.isclose(f(root1), 0, rel_tol=1e-9, abs_tol=1e-9)
    assert cmath.isclose(f(root2), 0, rel_tol=1e-9, abs_tol=1e-9)

    return root1, root2


# Example usage
if __name__ == "__main__":
    # Example: x^2 - 5x + 6 = 0  → roots are 2 and 3
    r1, r2 = quadratic_roots(1, -5, 6)
    print("Verified Roots:", r1, r2)

    # Example with complex roots: x^2 + x + 1 = 0
    r1, r2 = quadratic_roots(1, 1, 1)
    print("Verified Roots:", r1, r2)
