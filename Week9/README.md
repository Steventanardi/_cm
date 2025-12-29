# Week 9 - Information Theory and Coding

This project covers internal concepts of information theory, including entropy calculations, error-correcting codes, and fundamental communication theorems.

## Features
- **Probability Calculations**: Computing probabilities and log-probabilities of large-scale independent events (10,000 coin flips).
- **Information Metrics**: Implementation of Entropy, Cross-Entropy, KL Divergence, and Mutual Information using NumPy.
- **Verification**: Programmatic proof of Gibbs' Inequality ($H(P, P) \le H(P, Q)$).
- **Error Correction**: Implementation of a Hamming (7,4) Encoder and Decoder with single-bit error correction.

## Documentation
- **Theoretical Background**: A detailed explanation of Shannon's Source Coding Theorem and the Shannon-Hartley Theorem is provided in `explanation.md`.

## Attribution Statement
> [!IMPORTANT]
> **Authorship Status**: Original implementation.
> 
> - **Core Logic**: Fully original, implementing standard information theory formulas and Hamming coding matrices.
> - **AI Usage**: Developed with assistance for documentation and code structure optimization. 

## How to Run
Ensure you have NumPy installed:
```bash
pip install numpy
```

- Run information metrics: `python information_theory.py`
- Run Hamming code demo: `python hamming_code.py`
