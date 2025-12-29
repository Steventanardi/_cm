import numpy as np

# A simple 2-layer Neural Network implementation from scratch
# This demonstrates the math of feedforward and backpropagation

class SimpleNeuralNetwork:
    def __init__(self, input_size, hidden_size, output_size, learning_rate=0.1):
        # Initialize weights with random values
        self.W1 = np.random.randn(input_size, hidden_size)
        self.W2 = np.random.randn(hidden_size, output_size)
        # Initialize biases to zero
        self.b1 = np.zeros((1, hidden_size))
        self.b2 = np.zeros((1, output_size))
        self.learning_rate = learning_rate

    def sigmoid(self, x):
        return 1 / (1 + np.exp(-x))

    def sigmoid_derivative(self, x):
        return x * (1 - x)

    def forward(self, X):
        # Layer 1
        self.z1 = np.dot(X, self.W1) + self.b1
        self.a1 = self.sigmoid(self.z1)
        # Layer 2
        self.z2 = np.dot(self.a1, self.W2) + self.b2
        self.a2 = self.sigmoid(self.z2)
        return self.a2

    def backward(self, X, y, output):
        # Calculate error at output layer
        output_error = y - output
        output_delta = output_error * self.sigmoid_derivative(output)

        # Calculate error at hidden layer
        z1_error = output_delta.dot(self.W2.T)
        z1_delta = z1_error * self.sigmoid_derivative(self.a1)

        # Update weights and biases using Gradient Descent
        self.W2 += self.a1.T.dot(output_delta) * self.learning_rate
        self.W1 += X.T.dot(z1_delta) * self.learning_rate
        self.b2 += np.sum(output_delta, axis=0, keepdims=True) * self.learning_rate
        self.b1 += np.sum(z1_delta, axis=0, keepdims=True) * self.learning_rate

    def train(self, X, y, epochs=10000):
        for i in range(epochs):
            output = self.forward(X)
            self.backward(X, y, output)
            if i % 1000 == 0:
                loss = np.mean(np.square(y - output))
                print(f"Epoch {i}, Loss: {loss:.6f}")

if __name__ == "__main__":
    # Test on XOR problem
    X = np.array([[0,0], [0,1], [1,0], [1,1]])
    y = np.array([[0], [1], [1], [0]])

    nn = SimpleNeuralNetwork(input_size=2, hidden_size=4, output_size=1)
    print("Training Neural Network on XOR problem...")
    nn.train(X, y)

    print("\nPredictions after training:")
    predictions = nn.forward(X)
    for i in range(len(X)):
        print(f"Input: {X[i]}, Predicted: {predictions[i][0]:.4f}, Target: {y[i][0]}")
