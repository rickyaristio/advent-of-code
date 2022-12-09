import numpy as np
np.set_printoptions(threshold=np.inf)

def positionMovement(matrix_2d,move,steps,H_x,H_y,T_x,T_y):
    for n in range(steps):
        init_H_x = H_x
        init_H_y = H_y
        if(move == 'R'):
            H_x += 1 
        elif(move == 'U'):
            H_y += 1
        elif(move == 'L'):
            H_x -= 1
        elif(move == 'D'):
            H_y -= 1
        if((abs(H_x - T_x) > 1) or (abs(H_y - T_y) > 1)):
            T_x = init_H_x
            T_y = init_H_y
        matrix_2d[T_x][T_y] = True

    return matrix_2d,H_x,H_y,T_x,T_y
    

with open('input.txt', 'r') as f:
    lines = f.readlines()

matrix_2d = np.zeros((1000,1000))

H_x = 0
H_y = 0
T_x = 0
T_y = 0
count = 0

for line in lines:
    split = line.split()
    move = split[0]
    steps = int(split[1])

    matrix_2d,H_x,H_y,T_x,T_y = positionMovement(matrix_2d,move,steps,H_x,H_y,T_x,T_y)

count += int(np.sum(matrix_2d))
# print(matrix_2d)
print(count) #6642
