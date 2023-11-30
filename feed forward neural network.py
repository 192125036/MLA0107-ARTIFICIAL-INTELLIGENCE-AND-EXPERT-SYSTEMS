import numpy as np

# Define the sigmoid activation function
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# Define the derivative of the sigmoid function
def sigmoid_derivative(x):
    return x * (1 - x)

# Define the neural network class
class NeuralNetwork:
    def __init__(self, input_size, hidden_size, output_size):
        self.input_size = input_size
        self.hidden_size = hidden_size
        self.output_size = output_size

        # Initialize weights and biases randomly
        self.weights_input_hidden = np.random.rand(self.input_size, self.hidden_size)
        self.weights_hidden_output = np.random.rand(self.hidden_size, self.output_size)
        self.bias_hidden = np.random.rand(1, self.hidden_size)
        self.bias_output = np.random.rand(1, self.output_size)

    def forward(self, X):
        # Forward propagation through the network
        self.hidden_layer_input = np.dot(X, self.weights_input_hidden) + self.bias_hidden
        self.hidden_layer_output = sigmoid(self.hidden_layer_input)
        self.output_layer_input = np.dot(self.hidden_layer_output, self.weights_hidden_output) + self.bias_output
        self.output = sigmoid(self.output_layer_input)
        return self.output

    def backward(self, X, y, output):
        # Backpropagation to update weights and biases
        self.output_error = y - output
        self.output_delta = self.output_error * sigmoid_derivative(output)

        self.hidden_error = self.output_delta.dot(self.weights_hidden_output.T)
        self.hidden_delta = self.hidden_error * sigmoid_derivative(self.hidden_layer_output)

        self.weights_hidden_output += self.hidden_layer_output.T.dot(self.output_delta)
        self.weights_input_hidden += X.T.dot(self.hidden_delta)
        self.bias_output += np.sum(self.output_delta, axis=0)
        self.bias_hidden += np.sum(self.hidden_delta, axis=0)

    def train(self, X, y, epochs):
        for epoch in range(epochs):
            output = self.forward(X)
            self.backward(X, y, output)

# Example usage
# Input, output, and hidden layer sizes
input_size = 3
hidden_size = 4
output_size = 1

# Example dataset
X = np.array([[0, 1, 0],
              [1, 0, 1],
              [1, 1, 0],
              [0, 0, 1]])
y = np.array([[0], [1], [1], [0]])

# Create a neural network
nn = NeuralNetwork(input_size, hidden_size, output_size)

# Train the neural network
nn.train(X, y, epochs=10000)

# Predict using the trained model
predicted_output = nn.forward(X)
print("Predicted Output:")
print(predicted_output)
