import numpy as np
np.set_printoptions(threshold=np.inf)


def countSteps(count,matrix_2d,start,end):
    count_temp = 0
    pos = [start[0],start[0]]

    print(pos[0],pos[1])
    print(end[0],end[1])
    iter = 0

    while(pos[0] != end[0] or pos[1] != end[1]):

        if iter == 30:
            break
 
        #right
        if(pos[1]+1 >= 0 and pos[1]+1 <= len(matrix_2d[0])-1):
            if matrix_2d[pos[0]][pos[1]] == matrix_2d[pos[0]][pos[1]+1]-1 or matrix_2d[pos[0]][pos[1]] == matrix_2d[pos[0]][pos[1]+1]:
                count_temp += 1
                pos[1] = pos[1]+1
                print('right')
                iter += 1
                continue
        #down
        if(pos[0]+1 >= 0 and pos[0]+1 <= len(matrix_2d)-1):
            if matrix_2d[pos[0]][pos[1]] == matrix_2d[pos[0]+1][pos[1]]-1 or matrix_2d[pos[0]][pos[1]] == matrix_2d[pos[0]+1][pos[1]]:
                count_temp += 1
                pos[0] = pos[0]+1
                print('down')
                iter += 1
                continue
        #left
        if(pos[1]-1 >= 0 and pos[1]-1 <= len(matrix_2d[0])-1):
            if matrix_2d[pos[0]][pos[1]] == matrix_2d[pos[0]][pos[1]-1]-1 or matrix_2d[pos[0]][pos[1]] == matrix_2d[pos[0]][pos[1]-1]:
                count_temp += 1
                pos[1] = pos[1]-1
                print('left')
                iter += 1
                continue
        #up
        if(pos[0]-1 >= 0 and pos[0]-1 <= len(matrix_2d)-1):
            if matrix_2d[pos[0]][pos[1]] == matrix_2d[pos[0]-1][pos[1]]-1 or matrix_2d[pos[0]][pos[1]] == matrix_2d[pos[0]-1][pos[1]]:
                count_temp += 1
                pos[0] = pos[0]-1
                print('up')
                iter += 1
                continue
            
       
    
    count.append(count_temp)

    print('exit',count)

    

with open('input.txt', 'r') as f:
    lines = f.readlines()

matrix_2d = np.zeros((len(lines),len(lines[0])-1))
start = []
end = []

count = []

for i in range(len(lines)):
    for j in range(len(lines[0])-1):
        matrix_2d[i][j] = int(ord(lines[i][j])- 96)
        if(matrix_2d[i][j] == -13):
            start.append(i)
            start.append(j)
            matrix_2d[i][j] = 0
        elif(matrix_2d[i][j] == -27):
            end.append(i)
            end.append(j)
            matrix_2d[i][j] = 27

countSteps(count,matrix_2d,start,end)

print(matrix_2d)
# print(start,end)

# print(len(matrix_2d))
# print(len(matrix_2d[0]))
# # print(count) 


