# Conceptual Foundations of Linear Algebra

This document provides answers to the conceptual questions for Week 10.

## 1. Linearity and Algebra
- **Linearity**: Refers to properties of additivity $f(x+y) = f(x) + f(y)$ and homogeneity $f(cx) = cf(x)$. Visually, it represents straight lines or flat planes.
- **Algebra**: The study of mathematical symbols and the rules for manipulating them to solve equations.

## 2. Space and Vector Spaces
- **Space**: A set with added structure (like distance or direction).
- **Vector Space**: A collection of vectors that can be added together and multiplied by scalars while remaining within the same set. It is called a "space" because it defines the environment where geometric operations occur.

## 3. Matrices and Vectors
- **Vectors**: Represent points or directions in space.
- **Matrices**: Represent linear transformations (functions) that map vectors from one space to another. A matrix "acts" on a vector.

## 4. Transformations (2D/3D)
- **Translation**: Moves points by a vector (requires homogeneous coordinates).
- **Scaling**: Multiplies coordinates by factors (diagonal matrix).
- **Rotation**: Rotates points around the origin (using sine and cosine in the matrix).

## 5. Determinants and Volume
- **Determinant**: A scalar value that represents the "scaling factor" of a transformation.
- **Volume**: The absolute value of the determinant is the factor by which the transformation changes the area (2D) or volume (3D) of a shape.
- **Calculation**: Can be done recursively (Laplace expansion) or faster via LU decomposition (product of diagonal elements of $U$).

## 6. Eigenvalues and Eigenvectors
- **Eigenvector**: A vector that only changes by a scalar factor (magnitude) during a transformation; its direction remains the same.
- **Eigenvalue**: The factor by which the eigenvector is scaled.
- **Decomposition**: Used to diagonalize matrices and simplify complex linear systems.

## 7. QR Decomposition
- **Definition**: Decomposing a matrix into an orthogonal matrix $Q$ and an upper triangular matrix $R$.
- **Use**: Frequently used to solve the linear least squares problem and as a step in calculating eigenvalues.

## 8. SVD (Singular Value Decomposition)
- **Definition**: $A = U \Sigma V^T$.
- **Relation to Eigen**: $V$ are the eigenvectors of $A^T A$, and $U$ are the eigenvectors of $A A^T$. Singular values are the square roots of the eigenvalues.

## 9. PCA (Principal Component Analysis)
- **Definition**: A dimensionality reduction technique that finds the directions (principal components) of maximum variance in the data.
- **Relation to SVD**: PCA is typically performed by applying SVD to the centered data matrix. The principal components are the right singular vectors ($V$).
