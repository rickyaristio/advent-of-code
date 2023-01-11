import numpy as np

def checkLeftRight(matrix2d,i,j):
    if(matrix2d[i+1][j-1] > 0 and matrix2d[i+1][j+1] > 0):
        matrix2d[i][j] = 1
    elif(matrix2d[i+1][j-1] == 0):
        j = j-1
    elif(matrix2d[i+1][j+1] == 0):
        j = j+1
    return matrix2d,i,j
        

with open('input.txt', 'r') as f:
    lines = f.readlines()


#find matrix size
min_x = int((((lines[0].split())[0]).split(','))[1])
max_x = int((((lines[0].split())[0]).split(','))[1])
min_y = int((((lines[0].split())[0]).split(','))[0])
max_y = int((((lines[0].split())[0]).split(','))[0])

for line in lines:
    split_line = line.split()

    for n in range(0,len(split_line),2):
        
        if(n+2>len(split_line)):
            break

        y1 = int((split_line[n].split(','))[0])
        x1 = int((split_line[n].split(','))[1])
        y2 = int((split_line[n+2].split(','))[0])
        x2 = int((split_line[n+2].split(','))[1])

        if(min(x1,x2) < min_x):
            min_x = min(x1,x2)
        
        if(min(y1,y2) < min_y):
            min_y = min(y1,y2)

        if(max(x1,x2) > max_x):
            max_x = max(x1,x2)
        
        if(max(y1,y2) > max_y):
            max_y = max(y1,y2)

#create a field
matrix2d = np.zeros((max_x+1+2,(max_x+3)*2))

for line in lines:
    split_line = line.split()

    for n in range(0,len(split_line),2):
        
        if(n+2>len(split_line)):
            break

        y1 = int((split_line[n].split(','))[0])
        x1 = int((split_line[n].split(','))[1])
        y2 = int((split_line[n+2].split(','))[0])
        x2 = int((split_line[n+2].split(','))[1])

        dx = x2-x1
        dy = y2-y1

        if(dy == 0):
            if(dx > 0):
                for i in range(dx+1):
                    matrix2d[x1+i][y1-(500 - (max_x+3))] = 2
            elif(dx < 0):
                for i in range(-dx+1):
                    matrix2d[x2+i][y1-(500 - (max_x+3))] = 2
        elif(dx == 0):
            if(dy > 0):
                for i in range(dy+1):
                    matrix2d[x1][y1+i-(500 - (max_x+3))] = 2
            elif(dy < 0):
                for i in range(-dy+1):
                    matrix2d[x1][y2+i-(500 - (max_x+3))] = 2

for i in range(len(matrix2d[0])):
    matrix2d[max_x+2][i] = 2

#pouring the sand
coord_i = 0
coord_j = 500 - (500 - (max_x+3))
iter = 0
while(iter < 6000000):
    if(matrix2d[coord_i+1][coord_j] == 0):
        coord_i +=1
        continue
    elif(matrix2d[coord_i+1][coord_j] > 0):
        matrix2d,coord_i,coord_j = checkLeftRight(matrix2d,coord_i,coord_j)
        iter +=1
        # print(matrix2d,coord_i,coord_j)
        if(matrix2d[coord_i][coord_j] == 1): #reset
            coord_i = 0
            coord_j = 500-(500 - (max_x+3))
        if(matrix2d[0][(max_x+3)]):
            break      
        continue

print(matrix2d)
print(iter) #1568112

sum = 0
for i in range(len(matrix2d)):
    for j in range(len(matrix2d[0])):
        sum += matrix2d[i][j] % 2

print(int(sum)) #23416







