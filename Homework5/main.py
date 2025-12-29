from geometry import Point, Line, Circle, Triangle, intersect_lines, intersect_circles, intersect_line_circle, perpendicular_foot
import math

def main():
    print("--- Geometry Construction World ---\n")

    # 1. Define Point, Line, Circle
    p1 = Point(0, 0)
    p2 = Point(4, 0)
    p3 = Point(0, 3)
    
    line1 = Line(p1, p2) # y = 0
    line2 = Line(p1, p3) # x = 0
    circle1 = Circle(Point(2, 2), 2)
    circle2 = Circle(Point(4, 2), 2)

    print(f"Line 1: {line1}")
    print(f"Line 2: {line2}")
    print(f"Circle 1: {circle1}")
    print(f"Circle 2: {circle2}")

    # 2. Intersections
    print("\n--- Intersections ---")
    
    # Line-Line
    l3 = Line(Point(0, 4), Point(4, 0)) # x + y = 4
    l4 = Line(Point(0, 0), Point(4, 4)) # x - y = 0
    ll_int = intersect_lines(l3, l4)
    print(f"Intersection of {l3} and {l4}: {ll_int}")

    # Circle-Circle
    cc_int = intersect_circles(circle1, circle2)
    print(f"Intersection of Circle 1 and Circle 2: {cc_int}")

    # Line-Circle
    lc_int = intersect_line_circle(l3, circle1)
    print(f"Intersection of Line {l3} and Circle 1: {lc_int}")

    # 3. Perpendicular Line from Point to Line
    print("\n--- Perpendicular ---")
    pt_outside = Point(4, 4)
    foot = perpendicular_foot(line1, pt_outside)
    print(f"Perpendicular foot from {pt_outside} to {line1}: {foot}")

    # 4. Pythagorean Theorem Verification
    print("\n--- Pythagorean Theorem Verification ---")
    # Using Line (0,0) to (4,0), and Point (4,3)
    p_a = Point(0, 0)
    p_b = Point(4, 3)
    target_line = Line(p_a, Point(10, 0)) # x-axis
    p_c = perpendicular_foot(target_line, p_b) # Should be (4,0)
    
    # Triangle ABC is a right triangle at C
    a = math.dist([p_b.x, p_b.y], [p_c.x, p_c.y]) # Leg 1
    b = math.dist([p_a.x, p_a.y], [p_c.x, p_c.y]) # Leg 2
    c = math.dist([p_a.x, p_a.y], [p_b.x, p_b.y]) # Hypotenuse
    
    print(f"Point A: {p_a}, Point B: {p_b}, Foot C: {p_c}")
    print(f"Leg a (BC): {a:.2f}, Leg b (AC): {b:.2f}, Hypotenuse c (AB): {c:.2f}")
    print(f"a^2 + b^2 = {a**2 + b**2:.2f}")
    print(f"c^2 = {c**2:.2f}")
    if abs((a**2 + b**2) - c**2) < 1e-9:
        print("Pythagorean Theorem Verified!")

    # 5. Triangle Object
    print("\n--- Triangle ---")
    tri = Triangle(p_a, p_b, p_c)
    print(f"Original Triangle: {tri}")

    # 6. Transformations
    print("\n--- Transformations ---")
    translated_tri = tri.translate(10, 10)
    scaled_tri = tri.scale(2, 2, origin=p_a)
    rotated_tri = tri.rotate(90, origin=p_a)
    
    print(f"Translated (+10, +10): {translated_tri}")
    print(f"Scaled (x2) from Point A: {scaled_tri}")
    print(f"Rotated 90 degrees from Point A: {rotated_tri}")

if __name__ == "__main__":
    main()
