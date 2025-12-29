# Mathematics of the Geometry Library

This document explains the algorithms and formulas used in the `geometry.py` implementation.

## 1. Line Equation
All lines are converted to the standard form:
$$ Ax + By = C $$
Where:
- $A = y_2 - y_1$
- $B = x_1 - x_2$
- $C = Ax_1 + By_1$

## 2. Line-Line Intersection
Given two lines $A_1x + B_1y = C_1$ and $A_2x + B_2y = C_2$, the intersection is found using Cramer's Rule:
$$ x = \frac{C_1B_2 - C_2B_1}{A_1B_2 - A_2B_1}, \quad y = \frac{A_1C_2 - A_2C_1}{A_1B_2 - A_2B_1} $$

## 3. Perpendicular Foot
The foot of the perpendicular from $(x_0, y_0)$ to the line $Ax + By = C$ is:
$$ x = x_0 - \frac{A(Ax_0 + By_0 - C)}{A^2 + B^2} $$
$$ y = y_0 - \frac{B(Ax_0 + By_0 - C)}{A^2 + B^2} $$

## 4. Circle-Circle Intersection
The intersection of two circles with centers $(x_1, y_1), (x_2, y_2)$ and radii $r_1, r_2$ is found by calculating the distance $d$ between centers and finding the relative distance $a$ to the intersection chord:
$$ a = \frac{r_1^2 - r_2^2 + d^2}{2d} $$
The height of the intersection points from the line connecting the centers is:
$$ h = \sqrt{r_1^2 - a^2} $$

## 5. Transformations
- **Translation**: $(x, y) \to (x + dx, y + dy)$
- **Scaling**: $(x, y) \to (x_0 + (x - x_0) \cdot s_x, y_0 + (y - y_0) \cdot s_y)$
- **Rotation**:
  $$ x' = x_0 + (x - x_0) \cos \theta - (y - y_0) \sin \theta $$
  $$ y' = y_0 + (x - x_0) \sin \theta + (y - y_0) \cos \theta $$
