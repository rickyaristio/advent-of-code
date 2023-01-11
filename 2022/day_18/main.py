#credits: https://github.com/jornpe/Advent-of-Code-Python/blob/main/2022

with open('input.txt', 'r') as f:
    lines = f.readlines()

cells = []
x = []
y = []
z = []

for line in lines:
    split_line = line.split(',')
    xyz = (int(split_line[0]), int(split_line[1]), int(split_line[2]))
    cells.append(xyz)
    x.append(int(split_line[0]))
    y.append(int(split_line[1]))
    z.append(int(split_line[2]))

max_x = max(x)
max_y = max(y)
max_z = max(z)
max = max(max_x,max_y,max_z)

neighbours = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]

#part 1
count = 0
for x,y,z in cells:
    for dx,dy,dz in neighbours:
        if(x + dx, y + dy, z + dz) not in cells:
            count += 1
print(count) #3412

#part 2
count_2 = 0
visited = set()
queue = [(0,0,0)]

while queue:
    x,y,z = queue.pop(0)
    visited.add((x,y,z))
    for dx,dy,dz in neighbours:
        check = (x + dx, y + dy, z + dz)
        if -1 <= check[0] <= max+1 and -1 <= check[1] <= max+1 and -1 <= check[2] <= max+1 and check not in visited and check not in queue:
            if check in cells:
                count_2 += 1
            else:
                queue.append(check)

print(count_2) #2018
