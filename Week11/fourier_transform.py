import math
import numpy as np

def dft(f):
    """
    Discrete Fourier Transform (DFT)
    F(w) = sum_{x=0}^{N-1} f(x) * e^{-i * 2 * pi * w * x / N}
    """
    N = len(f)
    F = np.zeros(N, dtype=complex)
    for w in range(N):
        temp = 0
        for x in range(N):
            angle = -2j * math.pi * w * x / N
            temp += f[x] * np.exp(angle)
        F[w] = temp
    return F

def idft(F):
    """
    Inverse Discrete Fourier Transform (IDFT)
    f(x) = (1/N) * sum_{w=0}^{N-1} F(w) * e^{i * 2 * pi * w * x / N}
    """
    N = len(F)
    f_new = np.zeros(N, dtype=complex)
    for x in range(N):
        temp = 0
        for w in range(N):
            angle = 2j * math.pi * w * x / N
            temp += F[w] * np.exp(angle)
        f_new[x] = temp / N
    return f_new

if __name__ == "__main__":
    # 1. Define a sample signal f(x)
    # A simple sum of two sine waves: sin(2*pi*5*x/N) + 0.5*sin(2*pi*10*x/N)
    N = 64
    x = np.linspace(0, 1, N)
    f_original = np.sin(2 * np.pi * 5 * x) + 0.5 * np.sin(2 * np.pi * 12 * x)
    
    print("--- Fourier Transform Verification ---\n")
    print(f"Signal Length: {N}")
    
    # 2. Perform DFT
    print("Performing DFT...")
    F_freq = dft(f_original)
    
    # 3. Perform IDFT
    print("Performing IDFT...")
    f_reconstructed = idft(F_freq)
    
    # 4. Verify Reconstruction
    # Since the input was real, we take the real part of the reconstructed signal
    f_reconstructed_real = np.real(f_reconstructed)
    
    error = np.linalg.norm(f_original - f_reconstructed_real)
    print(f"\nReconstruction Error (L2 Norm): {error:.2e}")
    
    if error < 1e-10:
        print("Success: The original signal f was perfectly reconstructed from the frequency domain!")
    
    # Print sample comparison
    print("\nSample Values (Original vs Reconstructed):")
    for i in range(5):
        print(f"  x[{i}]: {f_original[i]:.4f} -> {f_reconstructed_real[i]:.4f}")
