input = [1, 2, 3, 4]

weights1 = [2.1, -0.5, 1.5, 1.7]
weights2 = [1.3, -0.6, -1.5, 3]
weights3 = [2, 4, -1.3, 3]
weights4 = [4, -2, 1.8, 2.9]

bias1 = 1
bias2 = 2
bias3 = 1.3
bias4 = 4

output = [input[0]*weights1[0] + input[1]*weights1[1] + input[2]*weights1[2] + input[3]*weights1[3] + bias1,
          input[0]*weights2[0] + input[1]*weights2[1] + input[2]*weights2[2] + input[3]*weights2[3] + bias2,
          input[0]*weights3[0] + input[1]*weights3[1] + input[2]*weights3[2] + input[3]*weights3[3] + bias3,
          input[0]*weights4[0] + input[1]*weights4[1] + input[2]*weights4[2] + input[3]*weights4[3] + bias4
]

print("Output : ", output)