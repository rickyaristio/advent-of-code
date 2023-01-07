#Kudos: https://github.com/viliampucik/adventofcode/blob/master/2022/

def solve(start,end,step):
    pos = set([start])

    # BFS
    while True:
        next_pos = set()
        for row, column in pos:
            for x,y in ((row,column),(row-1,column),(row+1,column),(row,column-1),(row,column+1)):
                if (x,y) == end:
                    return step
                
                if 0<= x < height and 0 <= y < width \
                   and grid[x][(y-step)%width] != ">" \
                   and grid[x][(y+step)%width] != "<" \
                   and grid[(x-step)%height][y] != "v" \
                   and grid[(x+step)%height][y] != "^":
                    next_pos.add((x,y))
        pos = next_pos
        if not pos: # wait 1 step
            pos.add(start)
        step +=1


with open('input.txt', 'r') as f:
    line = f.read().splitlines()

grid = []
for row in line[1:-1]:
    grid.append(row[1:-1])

height = len(grid)
width = len(grid[0])
start = (-1, 0) # x -> height, y -> width
end = (height, width - 1)

#task 1
trip_1 = solve(start,end,1)
print(trip_1) #334

#task 2
trip_2 = solve(end,start,trip_1)
print(trip_2) #643
trip_3 = solve(start,end,trip_2)
print(trip_3) #934