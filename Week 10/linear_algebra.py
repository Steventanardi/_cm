import numpy as np

# 1. Recursive Determinant Calculation
def determinant_recursive(matrix):
    n = len(matrix)
    if n == 1:
        return matrix[0][0]
    if n == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    
    det = 0
    for j in range(n):
        minor = [row[:j] + row[j+1:] for row in matrix[1:]]
        det += ((-1)**j) * matrix[0][j] * determinant_recursive(minor)
    return det

# 2. LU Decomposition
def lu_decomposition(A):
    n = A.shape[0]
    L = np.eye(n)
    U = A.copy().astype(float)
    
    for i in range(n):
        for j in range(i + 1, n):
            factor = U[j, i] / U[i, i]
            L[j, i] = factor
            U[j, i:] -= factor * U[i, i:]
    return L, U

def det_lu(A):
    _, U = lu_decomposition(A)
    return np.prod(np.diag(U))

# 3. SVD Using Eigenvalue Decomposition
def svd_from_eigen(A):
    # A = U S V^T
    # A^T A = V S^2 V^T
    # A A^T = U S^2 U^T
    ATA = np.dot(A.T, A)
    eigenvalues, V = np.linalg.eigh(ATA)
    
    # Sort in descending order
    idx = eigenvalues.argsort()[::-1]
    eigenvalues = eigenvalues[idx]
    V = V[:, idx]
    
    # Sigma matrix
    S = np.sqrt(np.clip(eigenvalues, 0, None))
    
    # Calculate U: u_i = A v_i / s_i
    U = np.zeros((A.shape[0], A.shape[1]))
    for i in range(len(S)):
        if S[i] > 1e-10:
            U[:, i] = np.dot(A, V[:, i]) / S[i]
            
    return U, S, V.T

# 4. PCA Using SVD
def pca_svd(X, num_components):
    # Center the data
    X_centered = X - np.mean(X, axis=0)
    U, S, Vt = svd_from_eigen(X_centered)
    
    # Principal components are the rows of Vt
    components = Vt[:num_components]
    projected = np.dot(X_centered, components.T)
    return projected, components

if __name__ == "__main__":
    # Test Matrix
    A = np.array([[4, 3], [6, 3]])
    print(f"--- Linear Algebra Verification ---\n")
    
    # Determinants
    det_rec = determinant_recursive(A.tolist())
    det_l_u = det_lu(A)
    print(f"1. Determinant (Recursive): {det_rec:.2f}")
    print(f"2. Determinant (LU): {det_l_u:.2f}")

    # Matrix Reconstruction
    print(f"\n3. Matrix Reconstructions (Check if error is near 0):")
    
    # LU
    L, U = lu_decomposition(A)
    recon_lu = np.dot(L, U)
    print(f"   LU Error: {np.linalg.norm(A - recon_lu):.2e}")
    
    # Eigen (using A^T A for symmetric example)
    sym_A = np.dot(A.T, A)
    evals, evecs = np.linalg.eigh(sym_A)
    recon_eigen = np.dot(evecs, np.dot(np.diag(evals), evecs.T))
    print(f"   Eigen (Symmetric) Error: {np.linalg.norm(sym_A - recon_eigen):.2e}")
    
    # SVD
    U_s, S_s, Vt_s = svd_from_eigen(A)
    recon_svd = np.dot(U_s, np.dot(np.diag(S_s), Vt_s))
    print(f"   SVD Error: {np.linalg.norm(A - recon_svd):.2e}")
    
    # PCA
    print(f"\n4. PCA Demonstration:")
    data = np.random.rand(10, 2)
    projected, components = pca_svd(data, 1)
    print(f"   Reduced 2D Data to 1D via PCA. Shape: {projected.shape}")
