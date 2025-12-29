# Week 11 - Manual Fourier Transform

This project implements the Discrete Fourier Transform (DFT) and its inverse (IDFT) from scratch in Python to demonstrate the transition between time and frequency domains.

## Features
- **Manual DFT**: Direct implementation of the Fourier summation formula without using external signal processing libraries.
- **Manual IDFT**: Recovery of the original signal from frequency components.
- **Verification**: Programmatic proof that $f(x) \rightarrow \text{DFT} \rightarrow \text{IDFT} \rightarrow f(x)$ maintains signal integrity.
- **Frequency Analysis**: Decomposition of complex signals into individual sine wave components.

## Documentation
- **Theoretical Background**: A detailed mathematical breakdown of the Fourier summation and Euler's formula is provided in `explanation.md`.

## Attribution Statement
> [!IMPORTANT]
> **Authorship Status**: Original implementation.
> 
> - **Core Logic**: Fully original. The DFT and IDFT algorithms were implemented manually to adhere to the "no packages" requirement.
> - **AI Usage**: Developed with assistance for mathematical explanations and code optimization.

## How to Run
```bash
python fourier_transform.py
```
The script will generate a sample waveform, transform it to the frequency domain, and verify the accuracy of the inverse transformation.
