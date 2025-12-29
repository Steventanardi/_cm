# Theory of Information and Communication

This document explains the key theorems and concepts in information theory.

## 1. Entropy (Information Content)
Entropy $H(X)$ measures the average amount of information produced by a stochastic source of data.
$$ H(X) = - \sum p(x) \log_2 p(x) $$

## 2. Shannon's Source Coding Theorem
This theorem establishes the fundamental limits to data compression. It states that, on average, a source cannot be compressed into fewer bits than its entropy without losing information.
- **Essence**: $H(X)$ is the absolute minimum average number of bits per symbol needed to represent the source.

## 3. Shannon-Hartley Theorem
This theorem tells us the maximum rate at which information can be transmitted over a communication channel of a certain bandwidth in the presence of noise.
$$ C = B \log_2(1 + \frac{S}{N}) $$
Where:
- $C$ is the channel capacity (bits per second).
- $B$ is the bandwidth of the channel (Hertz).
- $S$ is the average received signal power.
- $N$ is the average noise power.
- $S/N$ is the signal-to-noise ratio (SNR).

## 4. Hamming (7,4) Code
The Hamming (7,4) code is a block code that adds 3 parity bits to 4 data bits, creating a 7-bit codeword.
- **Capabilities**: It can detect and correct single-bit errors.
- **Distance**: It has a minimum Hamming distance of 3.
