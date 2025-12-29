# Mathematical Explanation of the Neural Network

This document explains the mathematical foundations of the Feedforward Neural Network implemented in `neural_network.py`.

## 1. Linear Transformation
Each layer performs a linear transformation on the input:
$$ Z = X \cdot W + b $$
where:
- $X$ is the input matrix.
- $W$ is the weight matrix.
- $b$ is the bias vector.

## 2. Activation Function (Sigmoid)
To introduce non-linearity, we use the Sigmoid function:
$$ \sigma(x) = \frac{1}{1 + e^{-x}} $$
Its derivative, used during backpropagation, is:
$$ \sigma'(x) = \sigma(x) \cdot (1 - \sigma(x)) $$

## 3. Backpropagation (Calculus / Chain Rule)
Backpropagation is the process of calculating the gradient of the loss function with respect to the weights. We use the chain rule to propagate the error from the output layer back to the input layer.

The gradient for the output weights $W_2$ is:
$$ \Delta W_2 = a_1^T \cdot (Error \cdot \sigma'(z_2)) $$

## 4. Gradient Descent
We update the weights by taking a step in the opposite direction of the gradient:
$$ W_{new} = W_{old} + \eta \cdot \Delta W $$
where $\eta$ is the learning rate.
