#Kudos: https://github.com/marcodelmastro/AdventOfCode2022/blob/main/

import numpy as np

with open('input.txt', 'r') as f:
    lines = f.read().split("\n\n")
    values = lines[0].split("\n")

x_max = max([len(value) for value in values])
y_max = len(values)
grid = np.zeros((y_max,x_max),dtype=int)-1

row = 0
for value in values:
    column = 0
    for item in value:
        if item == ".":
            grid[row][column] = 0
        elif item == "#":
            grid[row][column] = 2
        column += 1
    row += 1

instructions = lines[1].strip("\n")
moves = []
digit = ""
for item in instructions:
    if item.isdigit():
        digit += item
    if item == "R" or item == "L":
        moves.append(int(digit))
        moves.append(item)
        digit = ""
if digit != "":
    moves.append(int(digit))
      
##part 1
movements = [(1,0),(0,1),(-1,0),(0,-1)] #(>,v,<,^)

right = 0
down = 1
left = 2
up = 3

path = 1
wall = 2
wrap = -1

grid_x_max = grid.shape[1]
grid_y_max = grid.shape[0]
i_move = 0

#find starting point
x = 0
pos = set()
for p in grid[0]:
    if p == 0:
        pos = (x,0)
        break
    x += 1

for move in moves:
    if type(move) == int:
        pos_new = pos
        advance = True

        for item in range(move):
            pos_new = ((pos[0]+movements[i_move][0])%grid_x_max,(pos[1]+movements[i_move][1])%grid_y_max)
            xn,yn = pos_new
            if grid[yn][xn] == wall:
                break
            elif grid[yn][xn] == wrap:
                pos_old = pos
                while True:
                    pos_new = ((pos[0]+movements[i_move][0])%grid_x_max,(pos[1]+movements[i_move][1])%grid_y_max)
                    xn,yn = pos_new
                    if grid[yn][xn] == wall:
                        pos = pos_old
                        advance = False
                        break
                    if grid[yn][xn] != wrap:
                        break
                    pos = pos_new
            if advance:
                pos = pos_new
            else:
                break
    else:
        if move == "L":
            i_move = (i_move-1) % 4
        elif move == "R":
            i_move = (i_move+1) % 4

r = pos[1] + 1
c = pos[0] + 1
f = i_move
sum = 1000*r+4*c+f

print(sum) #60362
        

