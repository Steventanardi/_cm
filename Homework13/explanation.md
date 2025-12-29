# Theory of Homogeneous Linear ODEs with Constant Coefficients

This document explains the mathematical background and the implementation logic of the general ODE solver.

## 1. The Characteristic Equation
Consider a homogeneous linear differential equation of order $n$ with constant coefficients $a_i$:
$$ a_n y^{(n)} + a_{n-1} y^{(n-1)} + \dots + a_1 y' + a_0 y = 0 $$
By substituting $y = e^{\lambda x}$, we obtain the characteristic equation:
$$ a_n \lambda^n + a_{n-1} \lambda^{n-1} + \dots + a_1 \lambda + a_0 = 0 $$

The solution to the ODE depends on the roots $\lambda_i$ of this polynomial.

## 2. Types of Roots and Solutions

### Case 1: Distinct Real Roots
For each distinct real root $\lambda$, the term in the general solution is:
$$ C e^{\lambda x} $$

### Case 2: Repeated Real Roots
If a real root $\lambda$ has multiplicity $m$, it contributes $m$ linearly independent terms:
$$ (C_1 + C_2 x + C_3 x^2 + \dots + C_m x^{m-1}) e^{\lambda x} $$

### Case 3: Complex Conjugate Roots
Complex roots always appear in pairs $\alpha \pm i\beta$ for real coefficients. Each pair contributes:
$$ e^{\alpha x} (C_1 \cos(\beta x) + C_2 \sin(\beta x)) $$

### Case 4: Repeated Complex Roots
If a complex pair $\alpha \pm i\beta$ has multiplicity $m$, the terms are:
$$ e^{\alpha x} \sum_{k=0}^{m-1} x^k (A_k \cos(\beta x) + B_k \sin(\beta x)) $$

## 3. Implementation Details
The solver `solve_ode_general` follows these steps:
1. **Root Finding**: Uses `numpy.roots` to find numerical solutions.
2. **Tolerance Grouping**: Since high-order repeated roots are numerically unstable, a clustering approach with a tolerance of $10^{-4}$ is used to merge nearly identical roots.
3. **Classification**: Separates roots into real values and complex conjugate pairs.
4. **String Construction**: Dynamically builds the solution string $y(x)$, automatically formatting terms based on their types and multiplicities.
