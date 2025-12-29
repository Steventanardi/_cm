# MidTerm Math Project - Neural Network from Scratch

This project implements a simple 2-layer Feedforward Neural Network from scratch using Python and NumPy. It demonstrates the mathematical concepts of Linear Algebra and Calculus applied to machine learning.

## Features
- Implementation of feedforward propagation.
- Implementation of backpropagation using the chain rule.
- Training on the XOR logic gate problem.
- Detailed mathematical explanation included in `explanation.md`.

## Attribution Statement
> [!IMPORTANT]
> **Authorship Status**: Except for the neural network logic which was refined using AI assistance and online references, all parts of this project are original.
> 
> - **Core Logic**: Mostly original, but refined with AI assistance.
> - **References**: 
>   - Mathematical formulas for backpropagation: Wikipedia (Backpropagation).
>   - Coding structure: Inspired by neural network tutorials on *Towards Data Science*.
> - **AI Usage**: This project was developed with the assistance of an AI. Logic was optimized and documentation was refined.

## How to Run
Ensure you have NumPy installed:
```bash
pip install numpy
```

Run the main script:
```bash
python neural_network.py
```

## Mathematics Involved
- **Linear Algebra**: Matrix multiplication and dot products for layer transitions.
- **Calculus**: Partial derivatives and the chain rule for calculating weight updates (backpropagation).
- **Optimization**: Gradient Descent for minimizing the Mean Squared Error loss.
