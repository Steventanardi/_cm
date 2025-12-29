# finite_field.py
# A minimal Finite Field F_p (prime p) implementation with:
# - Field element class with operator overloading (+ - * /, ==)
# - Group-axiom checkers for (F, +) and (F\{0}, *)
# - Distributivity checker
# - Demo for F_7

from math import gcd

# ----------------------------
# Core: Extended Euclid inverse
# ----------------------------
def egcd(a, b):
    """Return (g, x, y) s.t. ax + by = g = gcd(a,b)."""
    if b == 0:
        return (a, 1, 0)
    g, x1, y1 = egcd(b, a % b)
    return (g, y1, x1 - (a // b) * y1)

def inv_mod(a, m):
    """Multiplicative inverse of a mod m (m must be prime or gcd(a,m)=1)."""
    a %= m
    if a == 0:
        raise ZeroDivisionError("0 has no multiplicative inverse.")
    g, x, _ = egcd(a, m)
    if g != 1:
        raise ZeroDivisionError(f"No inverse: gcd({a},{m})={g} != 1")
    return x % m

# ----------------------------
# Finite field element F_p
# ----------------------------
class Fp:
    __slots__ = ("val", "p")

    def __init__(self, val, p):
        if p < 2:
            raise ValueError("Modulus p must be >= 2.")
        self.p = int(p)
        self.val = int(val) % self.p

    # Pretty print
    def __repr__(self):
        return f"{self.val} (mod {self.p})"

    # Comparisons
    def __eq__(self, other):
        other = self._coerce(other)
        return self.p == other.p and self.val == other.val

    def __ne__(self, other):
        return not self.__eq__(other)

    # Unary
    def __neg__(self):
        return Fp(-self.val, self.p)

    # Binary ops
    def __add__(self, other):
        other = self._coerce(other)
        self._check_same_p(other)
        return Fp(self.val + other.val, self.p)

    def __sub__(self, other):
        other = self._coerce(other)
        self._check_same_p(other)
        return Fp(self.val - other.val, self.p)

    def __mul__(self, other):
        other = self._coerce(other)
        self._check_same_p(other)
        return Fp(self.val * other.val, self.p)

    def __truediv__(self, other):
        other = self._coerce(other)
        self._check_same_p(other)
        if other.val == 0:
            raise ZeroDivisionError("Division by zero in field.")
        return Fp(self.val * inv_mod(other.val, self.p), self.p)

    # Right-hand ops (allow int on left)
    __radd__ = __add__
    __rsub__ = lambda self, other: Fp(other, self.p) - self
    __rmul__ = __mul__
    __rtruediv__ = lambda self, other: Fp(other, self.p) / self

    # Helpers
    def _coerce(self, x):
        if isinstance(x, Fp):
            return x
        return Fp(x, self.p)

    def _check_same_p(self, other):
        if self.p != other.p:
            raise ValueError("Different moduli in operation.")

# ----------------------------
# Utilities to build a field
# ----------------------------
def is_prime(p):
    if p <= 3:
        return p >= 2
    if p % 2 == 0 or p % 3 == 0:
        return False
    i = 5
    while i * i <= p:
        if p % i == 0 or p % (i + 2) == 0:
            return False
        i += 6
    return True

class FiniteField:
    """A wrapper for F_p (prime p). Provides elements and verification helpers."""
    def __init__(self, p):
        if not is_prime(p):
            raise ValueError("p must be prime to form a field F_p.")
        self.p = int(p)

    def elem(self, a):
        return Fp(a, self.p)

    @property
    def zero(self):
        return self.elem(0)

    @property
    def one(self):
        return self.elem(1)

    def all_elements(self):
        return [self.elem(i) for i in range(self.p)]

    def nonzero_elements(self):
        return [self.elem(i) for i in range(1, self.p)]

# ----------------------------
# Axiom checkers
# ----------------------------
def check_group(elements, op, identity, inverse_fn, commutative=False):
    """
    elements: list of Fp
    op: function (a,b)->c
    identity: element
    inverse_fn: function a->a^{-1} wrt op
    commutative: set True to also verify commutativity
    """
    # Closure & associativity
    for a in elements:
        for b in elements:
            c = op(a, b)
            if c not in elements:
                raise AssertionError("Closure fails.")
            for d in elements:
                if op(op(a, b), d) != op(a, op(b, d)):
                    raise AssertionError("Associativity fails.")

    # Identity
    for a in elements:
        if op(a, identity) != a or op(identity, a) != a:
            raise AssertionError("Identity fails.")

    # Inverses
    for a in elements:
        inv = inverse_fn(a)
        if op(a, inv) != identity or op(inv, a) != identity:
            raise AssertionError("Inverse fails.")

    # Optional commutativity
    if commutative:
        for a in elements:
            for b in elements:
                if op(a, b) != op(b, a):
                    raise AssertionError("Commutativity fails.")

    return True

def check_distributivity(elements, add, mul):
    for a in elements:
        for b in elements:
            for c in elements:
                if mul(a, add(b, c)) != add(mul(a, b), mul(a, c)):
                    raise AssertionError("Left distributivity fails.")
                if mul(add(b, c), a) != add(mul(b, a), mul(c, a)):
                    raise AssertionError("Right distributivity fails.")
    return True

# ----------------------------
# Demo & self-test
# ----------------------------
if __name__ == "__main__":
    F = FiniteField(7)  # change 7 to any prime p

    E = F.all_elements()
    Ez = F.nonzero_elements()

    add = lambda x, y: x + y
    mul = lambda x, y: x * y

    add_inv = lambda x: -x
    mul_inv = lambda x: F.elem(inv_mod(x.val, F.p))  # only used on nonzero set

    print("Checking (F,+) is an abelian group...")
    assert check_group(E, add, F.zero, add_inv, commutative=True)
    print("OK")

    print("Checking (F\\{0},*) is an abelian group...")
    assert check_group(Ez, mul, F.one, mul_inv, commutative=True)
    print("OK")

    print("Checking distributivity...")
    assert check_distributivity(E, add, mul)
    print("OK")

    # Operator overloading demo
    a, b, c = F.elem(3), F.elem(5), F.elem(2)
    print("\nDemo in F_7:")
    print("a =", a, "b =", b, "c =", c)
    print("a + b =", a + b)
    print("a - b =", a - b)
    print("a * c =", a * c)
    print("b / c =", b / c)
    print("a * (b + c) =", a * (b + c))
    print("a*b + a*c =", a*b + a*c)
