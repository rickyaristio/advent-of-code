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
      
##part 2 (brute force --> can't run example with this)
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

###### square config
#   [1][2]
#   [3]
#[4][5]
#[6]
#####

print(pos)

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
                i_move_old = i_move

                #square [1] -> left [1] to left [4] reversed
                if xn==49 and 0<=yn<=49:
                    pos_new = (0, 149 - yn)
                    i_move = right
                #square [1] -> top [1] to left [6]
                if 50<=xn<=99 and yn==199:
                    pos_new = (0, xn + 100)
                    i_move = right
                
                #square [2] -> right [2] to right [5] reversed
                if xn==0 and 0<=yn<=49:
                    pos_new = (99, 149 - yn)
                    i_move = left
                #square [2] -> bottom [2] to right [3]
                if 100<=xn<=199 and yn==50:
                    pos_new = (99, xn - 50)
                    i_move = left
                #square [2] -> top [2] to bottom [6]
                if 100<=xn<=199 and yn==199:
                    pos_new = (xn - 100, 199)
                    i_move = up

                #square [3] -> right [3] to bottom [2]
                if xn==100 and 50<=yn<=99:
                    pos_new = (yn + 50, 49)
                    i_move = up
                #square [3] -> left [3] to top [4] !!
                if xn==49 and 50<=yn<=99:
                    pos_new = (yn - 50, 100)
                    i_move = down
                
                #square [4] -> top [4] to left [3]
                if 0<=xn<=49 and yn==99:
                    pos_new = (50, xn+50)
                    i_move = right
                #square [4] -> left [4] to left [1] reversed
                if xn==149 and 100<=yn<=149:
                    pos_new = (50, 149-yn)
                    i_move = right

                #square [5] -> right [5] to right [2] reversed
                if xn==100 and 100<=yn<=149:
                    pos_new = (149, 149-yn)
                    i_move = left
                #square [5] -> bottom [5] to right [3]
                if 50<=xn<=99 and yn==150:
                    pos_new = (49, xn+100)
                    i_move = left

                #square [6] -> left [6] to top [1]
                if xn==149 and 150<=yn<=199:
                    pos_new = (yn-100, 0)
                    i_move = down
                #square [6] -> right [6] to bottom [5]
                if xn==50 and 150<=yn<=199:
                    pos_new = (yn-100, 149)
                    i_move = up
                #square [6] -> bottom [6] to top [2]
                if 0<=xn<=49 and yn==0:
                    pos_new = (xn+100, 0)
                    i_move = down

                xn,yn = pos_new
                if grid[yn][xn] == wall:
                    pos = pos_old
                    i_move = i_move_old
                    advance = False
                    break

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

print(r,c,f,sum) #74288
        

