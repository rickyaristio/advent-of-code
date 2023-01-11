import numpy as np

with open('input.txt', 'r') as f:
    lines = f.readlines()

matrix = []
vector = []
for line in lines:
    for i in range(len(line)-1):
        vector.append(int(line[i]))
    matrix.append(vector)
    vector = []

count = len(matrix[0])*2 + len(lines)*2 - 4
print(count)


matrix_2d = np.zeros((len(matrix[0]),len(matrix[0])))
# print(matrix_2d)
# matrix_2d[1][1] = True
# print(int(np.sum(matrix_2d)))

left_max = 0
right_max = 0

#check row
for i in range(1,len(lines)-1):
    left_max = matrix[i][0]
    right_max = matrix[i][len(matrix[i])-1]
    for j in range(1,len(matrix[i])-1):
        if(matrix[i][j] > left_max):
            left_max = matrix[i][j]
            matrix_2d[i][j] = True
    for j in range(1,len(matrix[i])-1):
        if(matrix[i][len(matrix[i])-j-1] > right_max):
            right_max = matrix[i][len(matrix[i])-j-1]
            matrix_2d[i][len(matrix[i])-j-1] = True

upper_max = 0
lower_max = 0

#check column
for i in range(1,len(matrix[0])-1):
    upper_max = matrix[0][i]
    lower_max = matrix[len(matrix[i])-1][i]
    for j in range(1,len(matrix[0])-1):
        if(matrix[j][i] > upper_max):
            upper_max = matrix[j][i]
            matrix_2d[j][i] = True
    for j in range(1,len(matrix[0])-1):
        # if(matrix[len(matrix[i])-j][i] == 9):
        #     count += 1
        #     break
        if(matrix[len(matrix[i])-j-1][i] > lower_max):
            lower_max = matrix[len(matrix[i])-j-1][i]
            matrix_2d[len(matrix[i])-j-1][i] = True

count += int(np.sum(matrix_2d))
print(count) #1776


