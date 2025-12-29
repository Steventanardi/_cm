# Mathematics of the Fourier Transform

The Fourier Transform is a fundamental tool in mathematics and engineering used to decompose a function (usually a signal in the time domain) into its constituent frequencies.

## 1. Discrete Fourier Transform (DFT)
For a sequence of $N$ complex numbers $f(0), f(1), \dots, f(N-1)$, the DFT is defined as:
$$ F(w) = \sum_{x=0}^{N-1} f(x) e^{-i \cdot \frac{2\pi}{N} wx} $$
Where:
- $F(w)$ represents the amplitude and phase of the frequency component at index $w$.
- $x$ is the time/spatial index.
- $w$ is the frequency index.

## 2. Inverse Discrete Fourier Transform (IDFT)
The original sequence can be reconstructed from its frequency components using the IDFT:
$$ f(x) = \frac{1}{N} \sum_{w=0}^{N-1} F(w) e^{i \cdot \frac{2\pi}{N} wx} $$

## 3. Physical Intuition
- **Time Domain**: Represents how a signal changes over time ($f(x)$).
- **Frequency Domain**: Represents how much of each frequency is present in the signal ($F(w)$).
- **Euler's Formula**: The term $e^{i\theta} = \cos(\theta) + i\sin(\theta)$ allows us to represent oscillations as rotations in the complex plane.

## 4. Why implement from scratch?
By implementing these sums manually without using the Fast Fourier Transform (FFT) algorithm, we gain a direct understanding of the correlation between the signal and the complex sinusoids at each frequency. This method has a computational complexity of $O(N^2)$, whereas FFT is $O(N \log N)$.
