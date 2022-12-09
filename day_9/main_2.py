import numpy as np
np.set_printoptions(threshold=np.inf)

def positionMovement(matrix_2d,move,steps,T_x,T_y):
    for n in range(steps):
        if(move == 'R'):
            T_x[0] += 1 
        elif(move == 'U'):
            T_y[0] += 1
        elif(move == 'L'):
            T_x[0] -= 1
        elif(move == 'D'):
            T_y[0] -= 1
        for m in range(1,10):
            # print(m)
            if((T_x[m-1] - T_x[m] == 1 and T_y[m-1] - T_y[m] == 2) or (T_x[m-1] - T_x[m] == 2 and T_y[m-1] - T_y[m] == 1) or (T_x[m-1] - T_x[m] == 2 and T_y[m-1] - T_y[m] == 2)):
                T_x[m] += 1
                T_y[m] += 1
            elif((T_x[m-1] - T_x[m] == 1 and T_y[m-1] - T_y[m] == -2) or (T_x[m-1] - T_x[m] == 2 and T_y[m-1] - T_y[m] == -1) or (T_x[m-1] - T_x[m] == 2 and T_y[m-1] - T_y[m] == -2)):
                T_x[m] += 1
                T_y[m] -= 1
            elif((T_x[m-1] - T_x[m] == -1 and T_y[m-1] - T_y[m] == -2) or (T_x[m-1] - T_x[m] == -2 and T_y[m-1] - T_y[m] == -1) or (T_x[m-1] - T_x[m] == -2 and T_y[m-1] - T_y[m] == -2)):
                T_x[m] -= 1
                T_y[m] -= 1
            elif((T_x[m-1] - T_x[m] == -1 and T_y[m-1] - T_y[m] == 2) or (T_x[m-1] - T_x[m] == -2 and T_y[m-1] - T_y[m] == 1) or (T_x[m-1] - T_x[m] == -2 and T_y[m-1] - T_y[m] == 2)):
                T_x[m] -= 1
                T_y[m] += 1
            elif(T_x[m-1] - T_x[m] == 2):
                T_x[m] += 1
            elif(T_x[m-1] - T_x[m] == -2):
                T_x[m] -= 1
            elif(T_y[m-1] - T_y[m] == 2):
                T_y[m] += 1
            elif(T_y[m-1] - T_y[m] == -2):
                T_y[m] -= 1

        matrix_2d[T_x[9]+2500][T_y[9]+2500] = True
    return matrix_2d,T_x,T_y
    

with open('input.txt', 'r') as f:
    lines = f.readlines()

matrix_2d = np.zeros((5000,5000))

T_x = [0] * 10
T_y = [0] * 10
count = 0

for line in lines:
    split = line.split()
    move = split[0]
    steps = int(split[1])

    matrix_2d,T_x,T_y = positionMovement(matrix_2d,move,steps,T_x,T_y)

count += int(np.sum(matrix_2d))
# print(matrix_2d)
print(count) #6642 #... #2765


