import numpy as np
np.set_printoptions(threshold=np.inf)


def countSteps(matrix_2d,start,end):

    d = {(start[0],start[1]):{"shortest_distance":0,"previous":None}}
    queue = [(start[0],start[1])]

    while(len(queue)):

        i,j = queue.pop(0)
        previous = (i,j)
        shortest_distance = d[(i,j)]["shortest_distance"]

        for di,dj in [(0,-1),(-1,0),(0,1),(1,0)]:
            ni,nj = i+di,j+dj
          
            if ni < 0 or nj < 0:
                continue
            if ni>=len(matrix_2d) or nj>=len(matrix_2d[0]):
                continue
            if matrix_2d[ni][nj] - matrix_2d[i][j] > 1:
                continue
        
            if(ni,nj) not in d:
                d[(ni,nj)] = {"shortest_distance":shortest_distance+1,"previous":previous}
                queue.append((ni,nj))
            else:
                original_shortest_distance = d[(ni,nj)]["shortest_distance"]
                if shortest_distance + 1 < original_shortest_distance:
                    d[(ni,nj)] = {"shortest_distance":shortest_distance+1,"previous":previous}
            
    for x,y in d.items():
        print (x,y)


    out = {}
    path = []
    current = (end[0],end[1])
    while current != None:
        path.append(current)
        current = d[current]["previous"]
    out[(end[0],end[1])] = path[::-1]

    # print(out)
    print(len(path[::-1])-1) #474

    return len(path[::-1])-1


with open('input.txt', 'r') as f:
    lines = f.readlines()

matrix_2d = np.zeros((len(lines),len(lines[0])-1)).astype(int)
# starts = []
start = []
end = []

count = 0

for i in range(len(lines)):
    for j in range(len(lines[0])-1):
        matrix_2d[i][j] = int(ord(lines[i][j])- 96)
        if(matrix_2d[i][j] == -13):
            start.append(i)
            start.append(j)
            matrix_2d[i][j] = int(0)
        elif(matrix_2d[i][j] == -27):
            end.append(i)
            end.append(j)
            matrix_2d[i][j] = int(27)

count = countSteps(matrix_2d,start,end)
print(count) #474
