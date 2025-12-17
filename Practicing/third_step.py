import numpy as np


input = [1, 2, 3, 4]

weights = [[2.1, -0.5, 1.5, 1.7],
            [1.3, -0.6, -1.5, 3],
            [2, 4, -1.3, 3],
            [4, -2, 1.8, 2.9]]

biases = [1, 4, 2, 0.5]

output1 = np.dot(weights, input) + biases
output2 = np.dot(weights, input) + biases

print("Output 1 : ", output1)
print("Output 2 : ", output2)