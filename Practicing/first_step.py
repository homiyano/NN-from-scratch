input = [1.6, 2.5, 1.3] # input from last layer

# each neuron has weight and bias

weights = [2.1, 3.1, 1.6]

bias = 2

output = input[0] * weights[0] + input[1] * weights[1] + input[2] * weights[2] + bias

print(output)