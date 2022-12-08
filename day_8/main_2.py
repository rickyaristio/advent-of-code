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


matrix_3d = np.zeros((4,len(matrix[0]),len(matrix[0])))
# print(matrix_3d)

for i in range(1,len(lines)-1):
    for j in range(1,len(lines)-1):
        #left
        for k in range(j-1,-1,-1):
            matrix_3d[0][i][j] += 1
            if(matrix[i][k] >= matrix[i][j]):
                break
        #right
        for k in range(j+1,len(matrix[0])):
            # print(k)
            matrix_3d[1][i][j] += 1
            if(matrix[i][k] >= matrix[i][j]):
                break
        #up
        for k in range(i-1,-1,-1):
            # print(k)
            matrix_3d[2][i][j] += 1
            if(matrix[k][j] >= matrix[i][j]):
                break
        #down
        for k in range(i+1,len(matrix[0])):
            # print(k)
            matrix_3d[3][i][j] += 1
            if(matrix[k][j] >= matrix[i][j]):
                break

temp = 0
max = 0
for i in range(len(matrix[0])):
    for j in range(len(matrix[0])):
        temp = matrix_3d[0][i][j]*matrix_3d[1][i][j]*matrix_3d[2][i][j]*matrix_3d[3][i][j]
        if(temp > max):
            max = temp 

# print(matrix_3d)
print(int(max)) #234416

