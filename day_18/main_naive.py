import numpy as np
np.set_printoptions(linewidth=np.inf)


def checkNeighbour(number):
    return 6-2*number

with open('input.txt', 'r') as f:
    lines = f.readlines()

x = []
y = []
z = []

for line in lines:
    split_line = line.split(',')
    x.append(int(split_line[0]))
    y.append(int(split_line[1]))
    z.append(int(split_line[2]))

max_x = max(x)
max_y = max(y)
max = max(max_x,max_y)


#create a field
rows = max + 1 
cols = max + 1
matrix_2d = [[0 for c in range(cols)] for r in range(rows)]
for r in range(rows):
  for c in range(cols):
   matrix_2d[r][c]= []

sum = 0
for n in range(len(lines)):
    num_neighbor = 0

    #check z dir
    if not matrix_2d[x[n]][y[n]]: 
        matrix_2d[x[n]][y[n]].append(n+1)
    else:
        for m in range(len(matrix_2d[x[n]][y[n]])):
            if(abs(z[matrix_2d[x[n]][y[n]][m]-1] - z[n]) == 1):
                num_neighbor += 1
        matrix_2d[x[n]][y[n]].append(n+1)
    
    #check x-y dir
    for di,dj in [(0,-1),(-1,0),(0,1),(1,0)]:
        if x[n]+di < 0 or y[n]+dj < 0: #out of bounds
            continue
        if x[n]+di>=rows or y[n]+dj>=cols: #out of bounds
            continue
        if not matrix_2d[x[n]+di][y[n]+dj]:
            continue
        else:
            for m in range(len(matrix_2d[x[n]+di][y[n]+dj])):
                if(z[matrix_2d[x[n]+di][y[n]+dj][m]-1] == z[n]):
                    num_neighbor += 1
    
    print('turn',n, num_neighbor, checkNeighbour(num_neighbor))
    sum += checkNeighbour(num_neighbor)

print(sum)