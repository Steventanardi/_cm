# Week 10 - Linear Algebra: Algorithms and Concepts

This project implements fundamental linear algebra algorithms and explores the conceptual relationship between matrices, spaces, and data analysis.

## Implemented Algorithms
- **Determinant Calculation**: Manual recursive method (Laplace Expansion) and efficient LU Decomposition method.
- **Matrix Decompositions**: 
  - LU Decomposition ($A = LU$).
  - Singular Value Decomposition ($A = U \Sigma V^T$) derived from Eigenvalue decomposition.
- **Verification**: Programmatic verification of matrix reconstruction for LU, Eigen, and SVD.
- **Data Analysis**: 
  - Implementation of PCA (Principal Component Analysis) using SVD for dimensionality reduction.

## Documentation
- **Conceptual Q&A**: A detailed response to questions regarding linearity, determinants, and eigenvectors is provided in `concepts.md`.

## Attribution Statement
> [!IMPORTANT]
> **Authorship Status**: Original implementation.
> 
> - **Core Logic**: Manual implementation of matrix algorithms using NumPy for base operations.
> - **AI Usage**: Developed with assistance for conceptual summaries and documentation structure. All content is generated in English.

## How to Run
```bash
python linear_algebra.py
```
This script will perform calculations and verify the accuracy of the implemented decompositions.
