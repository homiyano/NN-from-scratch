import numpy as np

class Neuron:
    def __init__(self, input_dim):
        # initialize weights and bias
        self.w = np.random.randn(input_dim) * 0.01
        self.b = 0.0

    def forward(self, x):
        """
        x: shape (input_dim,)
        """
        z = np.dot(self.w, x) + self.b
        a = np.maximum(0, z)  # ReLU
        return z, a


x = np.array([2.0, -1.0])

neuron = Neuron(input_dim=2)

z, a = neuron.forward(x)

print("weights:", neuron.w)
print("bias:", neuron.b)
print("z:", z)
print("a (ReLU output):", a)
