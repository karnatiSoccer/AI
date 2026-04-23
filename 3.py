# Back propogation

import numpy as np

# Fix randomness (same output every time)
np.random.seed(1)

# Input and output (XOR)
x = np.array([[0,0],[0,1],[1,0],[1,1]])
y = np.array([[0],[1],[1],[0]])

# Initialize weights
w1 = np.random.rand(2,2)
w2 = np.random.rand(2,1)

# Learning rate
lr = 0.1

# Sigmoid function
def sigmoid(x):
    return 1/(1+np.exp(-x))

# Training
for i in range(10000):   # increased iterations
    
    # Forward propagation
    h = sigmoid(np.dot(x, w1))
    
    o = sigmoid(np.dot(h, w2))
    
    # Error
    error = y - o
    
    # Backpropagation
    d_o = error * o * (1 - o)
    d_h = d_o.dot(w2.T) * h * (1 - h)

    # Update weights
    w2 += lr * h.T.dot(d_o)
    w1 += lr * x.T.dot(d_h)

# Final Output
print("Predicted Output:")
print(o)

# Convert to 0 or 1
print("\nRounded Output:")
print(np.round(o))