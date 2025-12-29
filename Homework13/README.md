# Homework 13 - General ODE Solver

This project implements a general-purpose solver for homogeneous linear ordinary differential equations (ODEs) with constant coefficients.

## Features
- **General Solver**: A single function `solve_ode_general` that handles any order of homogeneous ODEs.
- **Root Classification**: Automatically detects and groups:
  - Distinct real roots.
  - Repeated real roots (multiplicity > 1).
  - Complex conjugate pairs.
  - Repeated complex conjugate pairs.
- **Numerical Stability**: Implements tolerance-based root clustering to ensure accurate multiplicity detection even for unstable high-order repeated roots.
- **Formatted Output**: Generates human-readable solution strings in the form $y(x) = \sum C_i f_i(x)$.

## Documentation
- **Theoretical Background**: A detailed mathematical breakdown of the characteristic equation and solution types is provided in `explanation.md`.

## Attribution Statement
> [!IMPORTANT]
> **Authorship Status**: Original implementation.
> 
> - **Core Logic**: Manual implementation using NumPy for characteristic root finding and custom string construction for the general solution.
> - **AI Usage**: Developed with assistance for algorithm optimization and documentation formatting.

## How to Run
```bash
python solve_ode.py
```
This script includes several test cases demonstrating the solver's ability to handle various root scenarios.
