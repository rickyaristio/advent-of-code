import numpy as np

def checkLeftRight(matrix2d,i,j):
    # print(i,j)
    # print(matrix2d[i][j-1],matrix2d[i+1][j-1])
    # print(matrix2d[i][j+1],matrix2d[i+1][j+1])
    if(matrix2d[i+1][j-1] > 0 and matrix2d[i+1][j+1] > 0):
        # print('yo2')
        matrix2d[i][j] = 1
    elif(matrix2d[i+1][j-1] == 0):
        # print('yo3')
        j = j-1
    elif(matrix2d[i+1][j+1] == 0):
        # print('yo4')
        j = j+1
    return matrix2d,i,j
        

with open('input.txt', 'r') as f:
    lines = f.readlines()

#create a field
matrix2d = np.zeros((10,10))
max_path = int((((lines[0].split())[0]).split(','))[1])
for line in lines:
    split_line = line.split()

    for n in range(0,len(split_line),2):
        
        if(n+2>len(split_line)):
            break

        y1 = int((split_line[n].split(','))[0])
        x1 = int((split_line[n].split(','))[1])
        y2 = int((split_line[n+2].split(','))[0])
        x2 = int((split_line[n+2].split(','))[1])

        if(min(x1,x2) < max_path):
            max_path = min(x1,x2)

        dx = x2-x1
        dy = y2-y1

        if(dy == 0):
            if(dx > 0):
                for i in range(dx+1):
                    matrix2d[x1+i][y1-494] = 2
            elif(dx < 0):
                for i in range(-dx+1):
                    matrix2d[x2+i][y1-494] = 2
        elif(dx == 0):
            if(dy > 0):
                for i in range(dy+1):
                    matrix2d[x1][y1+i-494] = 2
            elif(dy < 0):
                for i in range(-dy+1):
                    matrix2d[x1][y2+i-494] = 2

# print(matrix2d)
# print(len(matrix2d))
# print(max_path)

#pouring the sand

coord_i = 0
coord_j = 500 - 494
iter = 0
while(iter < 51):
    if(matrix2d[coord_i+1][coord_j] == 0):
        coord_i +=1
        continue
    elif(matrix2d[coord_i+1][coord_j] > 0):
        matrix2d,coord_i,coord_j = checkLeftRight(matrix2d,coord_i,coord_j)
        iter +=1
        # print(matrix2d,coord_i,coord_j)
        if(matrix2d[coord_i][coord_j] == 1): #reset
            coord_i = 0
            coord_j = 500-494        
        continue

print(matrix2d)

sum = 0
for i in range(len(matrix2d)):
    for j in range(len(matrix2d[0])):
        sum += matrix2d[i][j] % 2

print(int(sum))







