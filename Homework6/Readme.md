# Week 3 – Geometry: Constructing the World of Points, Lines, and Circles

## 1. Introduction
This project implements a small Python geometry library to explore the concepts of **points, lines, and circles**.  
The code demonstrates:
- Intersections between lines, circles, and line–circle.
- Perpendicular construction through a point.
- Verification of the Pythagorean theorem.
- Triangle object creation.
- Geometric transformations: translation, scaling, rotation.

## 2. Definitions
- **Point**: An object with coordinates (x, y).  
- **Line**: An infinite straight path determined by a point and a direction vector.  
- **Circle**: The set of all points at a fixed distance (radius) from a center point.  

## 3. Program Structure
- `Point`: Implements coordinates, vector operations, distance, rotation, scaling, translation.  
- `Line`: Represents a line; includes projection, perpendicular line construction.  
- `Circle`: Represents a circle with center and radius.  
- `Triangle`: Object defined by three points; includes centroid, side lengths, and transformations.  

### Key Functions
- `intersect_lines(L1, L2)`: Intersection of two lines.  
- `intersect_line_circle(L, C)`: Intersection of a line and a circle.  
- `intersect_circles(C1, C2)`: Intersection of two circles.  
- `verify_pythagoras(A, B, X)`: Verifies Pythagorean theorem using projection.  

## 4. Verification of Pythagoras Theorem
Given line AB and an external point X:
1. Project X onto AB to get foot H.  
2. Check numerically that:  
   \[
   |AX|^2 = |AH|^2 + |HX|^2
   \]  
3. Program outputs both sides and confirms they are equal (within tolerance).  

## 5. Transformations on Triangle
- **Translation**: Move triangle by (dx, dy).  
- **Scaling**: Enlarge or shrink triangle about a reference point.  
- **Rotation**: Rotate triangle about a reference point by θ radians.  

## 6. How to Run
```bash
python geometry.py
