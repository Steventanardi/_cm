# geometry.py
# A tiny geometry toolkit: Points, Lines, Circles, Triangles
# Includes:
# - Intersections: line-line, circle-circle, line-circle
# - Perpendicular through a point to a line
# - Pythagorean theorem numerical verification
# - Triangle object with translate / scale / rotate
# All computations use float with a small tolerance EPS.

from math import hypot, isclose, atan2, cos, sin

EPS = 1e-9

# ---------- Core primitives ----------

class Point:
    __slots__ = ("x", "y")
    def __init__(self, x: float, y: float):
        self.x = float(x); self.y = float(y)

    def __repr__(self): return f"Point({self.x:.6g}, {self.y:.6g})"
    def __iter__(self): yield self.x; yield self.y

    # vector ops
    def __add__(self, other):  return Point(self.x + other.x, self.y + other.y)
    def __sub__(self, other):  return Point(self.x - other.x, self.y - other.y)
    def __mul__(self, k: float): return Point(self.x * k, self.y * k)
    __rmul__ = __mul__
    def __truediv__(self, k: float): return Point(self.x / k, self.y / k)

    def dot(self, other):  return self.x*other.x + self.y*other.y
    def cross(self, other):  return self.x*other.y - self.y*other.x  # z-component
    def norm(self):  return hypot(self.x, self.y)
    def distance(self, other):  return (self - other).norm()

    def rotated(self, theta_rad: float, about=None):
        """Rotate by theta (radians) about 'about' (Point or None for origin)."""
        if about is None: about = Point(0, 0)
        p = self - about
        c, s = cos(theta_rad), sin(theta_rad)
        return Point(c*p.x - s*p.y, s*p.x + c*p.y) + about

    def translated(self, dx: float, dy: float):
        return Point(self.x + dx, self.y + dy)

    def scaled(self, sx: float, sy: float=None, about=None):
        """Scale by sx (and sy if given) about point 'about' (default origin)."""
        if about is None: about = Point(0, 0)
        if sy is None: sy = sx
        p = self - about
        return Point(p.x * sx, p.y * sy) + about


class Line:
    """
    Line represented by point P and direction vector V (non-zero).
    Equation: P + t*V. Also exposes (a,b,c) with ax + by + c = 0.
    """
    __slots__ = ("P", "V")
    def __init__(self, P: Point, Q_or_V: Point):
        self.P = P
        self.V = Q_or_V if isinstance(Q_or_V, Point) else Point(*Q_or_V)
        if isclose(self.V.norm(), 0.0, abs_tol=EPS):
            raise ValueError("Direction vector cannot be zero.")

    def __repr__(self): return f"Line(P={self.P}, V={self.V})"

    @property
    def a_b_c(self):
        # normal vector n = ( -Vy, Vx )
        a, b = -self.V.y, self.V.x
        c = -(a*self.P.x + b*self.P.y)
        return a, b, c

    def project(self, X: Point) -> Point:
        """Orthogonal projection of X onto this line."""
        w = X - self.P
        t = w.dot(self.V) / self.V.dot(self.V)
        return self.P + self.V * t

    def perpendicular_through(self, X: Point) -> "Line":
        """Line through X perpendicular to this line."""
        # dir vector perpendicular to V is n = (-Vy, Vx)
        n = Point(-self.V.y, self.V.x)
        return Line(X, n)


class Circle:
    __slots__ = ("C", "r")
    def __init__(self, C: Point, r: float):
        if r < 0: raise ValueError("Radius must be non-negative.")
        self.C = C; self.r = float(r)

    def __repr__(self): return f"Circle(C={self.C}, r={self.r:.6g})"

# ---------- Intersections ----------

def intersect_lines(L1: Line, L2: Line):
    """
    Intersection of two (infinite) lines.
    Returns:
      - [] if parallel and distinct,
      - [Point] if a unique intersection,
      - None if coincident (infinitely many).
    """
    p, r = L1.P, L1.V
    q, s = L2.P, L2.V
    rxs = r.cross(s)
    if abs(rxs) < EPS:
        # parallel
        if abs((q - p).cross(r)) < EPS:
            return None  # coincident
        return []
    t = (q - p).cross(s) / rxs
    return [p + r * t]

def intersect_line_circle(L: Line, C: Circle):
    """
    Intersection of an infinite line and a circle.
    Returns [] (no point), [P] (tangent), or [P1, P2].
    """
    # Move to line-param form: P(t) = P0 + t*v
    P0, v = L.P, L.V
    # Vector from center to line point
    u = P0 - C.C
    # Solve |u + t v|^2 = r^2 => (v·v)t^2 + 2(u·v)t + (u·u - r^2) = 0
    A = v.dot(v)
    B = 2 * u.dot(v)
    D = u.dot(u) - C.r*C.r
    # Quadratic
    disc = B*B - 4*A*D
    if disc < -EPS:  # no real intersection
        return []
    if abs(disc) <= EPS:
        t = -B / (2*A)
        return [P0 + v*t]
    sqrt_disc = disc**0.5
    t1 = (-B + sqrt_disc) / (2*A)
    t2 = (-B - sqrt_disc) / (2*A)
    return [P0 + v*t1, P0 + v*t2]

def intersect_circles(C1: Circle, C2: Circle):
    """
    Intersection of two circles.
    Returns [] (none), [P] (tangent), or [P1, P2].
    """
    d = C1.C.distance(C2.C)
    r1, r2 = C1.r, C2.r
    if d < EPS and abs(r1 - r2) < EPS:
        return None  # coincident circles (infinitely many intersections)
    if d > r1 + r2 + EPS or d < abs(r1 - r2) - EPS:
        return []  # separate or contained
    # distance from C1 to line of centers' intersection foot
    a = (r1*r1 - r2*r2 + d*d) / (2*d)
    h_sq = r1*r1 - a*a
    if h_sq < 0 and abs(h_sq) < 1e-12:  # clamp tiny neg due to FP
        h_sq = 0.0
    if h_sq < 0: return []  # numerical safety
    h = h_sq**0.5

    # point P along the center line
    ex = (C2.C - C1.C) / d
    P = C1.C + ex * a
    if h == 0:
        return [P]  # tangent
    # perpendicular vector
    ey = Point(-ex.y, ex.x)
    return [P + ey*h, P - ey*h]

# ---------- Pythagorean verification ----------

def verify_pythagoras(A: Point, B: Point, X: Point, tol=1e-7):
    """
    Given line AB and an external point X, drop perpendicular from X to AB.
    Let H be the foot. Check |AX|^2 = |AH|^2 + |HX|^2 (right triangle at H).
    Returns (H, ok_bool, lhs, rhs).
    """
    L = Line(A, B - A)
    H = L.project(X)
    lhs = A.distance(X)**2
    rhs = A.distance(H)**2 + H.distance(X)**2
    ok = isclose(lhs, rhs, rel_tol=0, abs_tol=tol)
    return H, ok, lhs, rhs

# ---------- Triangle with transformations ----------

class Triangle:
    __slots__ = ("A", "B", "C")
    def __init__(self, A: Point, B: Point, C: Point):
        self.A, self.B, self.C = A, B, C

    def __repr__(self): return f"Triangle({self.A}, {self.B}, {self.C})"

    def vertices(self): return [self.A, self.B, self.C]
    def side_lengths(self):
        a = self.B.distance(self.C)  # length opposite A
        b = self.A.distance(self.C)  # opposite B
        c = self.A.distance(self.B)  # opposite C
        return a, b, c

    def centroid(self):
        return Point((self.A.x+self.B.x+self.C.x)/3.0, (self.A.y+self.B.y+self.C.y)/3.0)

    def translated(self, dx: float, dy: float):
        return Triangle(self.A.translated(dx,dy), self.B.translated(dx,dy), self.C.translated(dx,dy))

    def scaled(self, sx: float, sy: float=None, about: Point=None):
        return Triangle(self.A.scaled(sx, sy, about), self.B.scaled(sx, sy, about), self.C.scaled(sx, sy, about))

    def rotated(self, theta_rad: float, about: Point=None):
        return Triangle(self.A.rotated(theta_rad, about), self.B.rotated(theta_rad, about), self.C.rotated(theta_rad, about))


# ---------- Demo covering the assignment items ----------

if __name__ == "__main__":
    print("=== Basic objects ===")
    P = Point(0, 0); Q = Point(4, 0); R = Point(1, 3)
    L1 = Line(P, Q - P)
    L2 = Line(Point(0, 1), Point(1, 2) - Point(0,1))
    C1 = Circle(Point(1, 0), 2); C2 = Circle(Point(3, 1), 2)
    print(P, Q, R)
    print(L1)
    print(C1)

    print("\n=== Intersections ===")
    print("Line-Line:", intersect_lines(L1, L2))
    print("Line-Circle:", intersect_line_circle(L1, C1))
    print("Circle-Circle:", intersect_circles(C1, C2))

    print("\n=== Perpendicular construction ===")
    perp = L1.perpendicular_through(R)
    H = L1.project(R)
    print("Perpendicular through R:", perp)
    print("Foot of perpendicular H:", H)

    print("\n=== Verify Pythagorean Theorem ===")
    H2, ok, lhs, rhs = verify_pythagoras(P, Q, R)
    print(f"H={H2},  |AX|^2={lhs:.6g},  |AH|^2+|HX|^2={rhs:.6g},  OK? {ok}")

    print("\n=== Triangle & transformations ===")
    T = Triangle(P, Q, R)
    print("Triangle T:", T, "side lengths:", tuple(f'{s:.4f}' for s in T.side_lengths()))
    T_shift = T.translated(2, 1)
    T_scaled = T.scaled(0.5, about=T.centroid())
    T_rot = T.rotated(0.5, about=T.centroid())
    print("T translated:", T_shift)
    print("T scaled (about centroid):", T_scaled)
    print("T rotated (about centroid, 0.5 rad):", T_rot)

    print("\nAll done.")
