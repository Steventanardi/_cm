import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def translate(self, dx, dy):
        return Point(self.x + dx, self.y + dy)

    def scale(self, sx, sy, origin=None):
        if origin is None:
            origin = Point(0, 0)
        return Point(
            origin.x + (self.x - origin.x) * sx,
            origin.y + (self.y - origin.y) * sy
        )

    def rotate(self, angle_deg, origin=None):
        if origin is None:
            origin = Point(0, 0)
        angle_rad = math.radians(angle_deg)
        cos_a = math.cos(angle_rad)
        sin_a = math.sin(angle_rad)
        
        dx = self.x - origin.x
        dy = self.y - origin.y
        
        new_x = origin.x + dx * cos_a - dy * sin_a
        new_y = origin.y + dx * sin_a + dy * cos_a
        return Point(new_x, new_y)

    def __repr__(self):
        return f"Point({self.x:.2f}, {self.y:.2f})"

class Line:
    # Defined by two points P1 and P2
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def get_coefficients(self):
        # Ax + By = C
        A = self.p2.y - self.p1.y
        B = self.p1.x - self.p2.x
        C = A * self.p1.x + B * self.p1.y
        return A, B, C

    def translate(self, dx, dy):
        return Line(self.p1.translate(dx, dy), self.p2.translate(dx, dy))

    def scale(self, sx, sy, origin=None):
        return Line(self.p1.scale(sx, sy, origin), self.p2.scale(sx, sy, origin))

    def rotate(self, angle_deg, origin=None):
        return Line(self.p1.rotate(angle_deg, origin), self.p2.rotate(angle_deg, origin))

    def __repr__(self):
        return f"Line({self.p1}, {self.p2})"

class Circle:
    def __init__(self, center, radius):
        self.center = center
        self.radius = radius

    def translate(self, dx, dy):
        return Circle(self.center.translate(dx, dy), self.radius)

    def scale(self, s, origin=None):
        # Uniform scaling for circle radius
        return Circle(self.center.scale(s, s, origin), self.radius * s)

    def rotate(self, angle_deg, origin=None):
        return Circle(self.center.rotate(angle_deg, origin), self.radius)

    def __repr__(self):
        return f"Circle(Center={self.center}, Radius={self.radius:.2f})"

class Triangle:
    def __init__(self, p1, p2, p3):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3

    def translate(self, dx, dy):
        return Triangle(self.p1.translate(dx, dy), self.p2.translate(dx, dy), self.p3.translate(dx, dy))

    def scale(self, sx, sy, origin=None):
        return Triangle(self.p1.scale(sx, sy, origin), self.p2.scale(sx, sy, origin), self.p3.scale(sx, sy, origin))

    def rotate(self, angle_deg, origin=None):
        return Triangle(self.p1.rotate(angle_deg, origin), self.p2.rotate(angle_deg, origin), self.p3.rotate(angle_deg, origin))

    def __repr__(self):
        return f"Triangle({self.p1}, {self.p2}, {self.p3})"

def intersect_lines(l1, l2):
    A1, B1, C1 = l1.get_coefficients()
    A2, B2, C2 = l2.get_coefficients()
    
    det = A1 * B2 - A2 * B1
    if abs(det) < 1e-10:
        return None  # Parallel
    
    x = (B2 * C1 - B1 * C2) / det
    y = (A1 * C2 - A2 * C1) / det
    return Point(x, y)

def perpendicular_foot(line, point):
    A, B, C = line.get_coefficients()
    # Foot of perpendicular from (x0, y0) to Ax + By = C
    # x = x0 - A(Ax0 + By0 - C) / (A^2 + B^2)
    # y = y0 - B(Ax0 + By0 - C) / (A^2 + B^2)
    denom = A*A + B*B
    if denom == 0: return None
    
    dist_val = A * point.x + B * point.y - C
    px = point.x - A * dist_val / denom
    py = point.y - B * dist_val / denom
    return Point(px, py)

def intersect_line_circle(line, circle):
    A, B, C = line.get_coefficients()
    # Normalize center to origin conceptually
    cx, cy = circle.center.x, circle.center.y
    r = circle.radius
    
    # Distance from center to line
    dist = abs(A * cx + B * cy - C) / math.sqrt(A*A + B*B)
    
    if dist > r:
        return [] # No intersection
    
    # Foot of perpendicular from center to line
    foot = perpendicular_foot(line, circle.center)
    
    if abs(dist - r) < 1e-10:
        return [foot] # Tangent
        
    # Intersection points
    d_offset = math.sqrt(r*r - dist*dist)
    # Direction vector of line
    dx = line.p2.x - line.p1.x
    dy = line.p2.y - line.p1.y
    line_len = math.sqrt(dx*dx + dy*dy)
    ux, uy = dx/line_len, dy/line_len
    
    p1 = Point(foot.x + ux * d_offset, foot.y + uy * d_offset)
    p2 = Point(foot.x - ux * d_offset, foot.y - uy * d_offset)
    return [p1, p2]

def intersect_circles(c1, c2):
    dx = c2.center.x - c1.center.x
    dy = c2.center.y - c1.center.y
    d = math.sqrt(dx*dx + dy*dy)
    
    if d > c1.radius + c2.radius or d < abs(c1.radius - c2.radius) or d == 0:
        return [] # No intersection or one inside another or same center
        
    a = (c1.radius**2 - c2.radius**2 + d**2) / (2 * d)
    h = math.sqrt(max(0, c1.radius**2 - a**2))
    
    x2 = c1.center.x + a * (c2.center.x - c1.center.x) / d
    y2 = c1.center.y + a * (c2.center.y - c1.center.y) / d
    
    p1 = Point(x2 + h * (c2.center.y - c1.center.y) / d, y2 - h * (c2.center.x - c1.center.x) / d)
    p2 = Point(x2 - h * (c2.center.y - c1.center.y) / d, y2 + h * (c2.center.x - c1.center.x) / d)
    
    if h == 0:
        return [p1]
    return [p1, p2]
