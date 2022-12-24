#credits: https://www.reddit.com/r/adventofcode/comments/znykq2/comment/j0oh1ti/?utm_source=share&utm_medium=web2x&context=3

class Shape:
    def __init__(self,shape):
        self.space = []
        self.landed = False
        for n in range(4):
            self.space.append([0,0,0,0])
        if shape == 'horizontal':
            self.space[0][0] = 1
            self.space[0][1] = 1
            self.space[0][2] = 1
            self.space[0][3] = 1
            self.width = 4
        elif shape == 'cross':
            self.space[0][1] = 1
            self.space[1][0] = 1
            self.space[1][1] = 1
            self.space[1][2] = 1
            self.space[2][1] = 1
            self.width = 3
        elif shape == 'L':
            self.space[0][0] = 1
            self.space[0][1] = 1
            self.space[0][2] = 1
            self.space[1][2] = 1
            self.space[2][2] = 1
            self.width = 3
        elif shape == 'vertical':
            self.space[0][0] = 1
            self.space[1][0] = 1
            self.space[2][0] = 1
            self.space[3][0] = 1
            self.width = 1
        elif shape == 'square':
            self.space[0][0] = 1
            self.space[0][1] = 1
            self.space[1][0] = 1
            self.space[1][1] = 1
            self.width = 2
    
    def move(self, direction, x, y, space):
        move = True

        if direction == 'v':
            for i in range(4):
                for j in range(4):
                    if self.space[i][j] == 1 and space[i+y-1][j+x] ==1:
                        move = False
            if move == True:
                return x,y -1
            self.landed = True
            return x,y

        if direction == '<':
            dx = -1
        elif direction == '>':
            dx = 1
        
        for i in range(4):
            for j in range(4):
                if self.space[i][j] == 1 and space[i+y][j+x+dx] ==1:
                    move = False
        if move == True:
            return x+dx,y
        return x,y

def run(iterations):
    field = [[1,1,1,1,1,1,1,1,1]]
    for i in range(iterations*4):
        field.append([1,0,0,0,0,0,0,0,1])
    
    top_rock = 0
    input = 0
    starts = {}
    for n in range(iterations):
        input = input % len(inputs) 
        if n % len(order) == 0 and field[top_rock][5] == 1:
            if input in starts:
                starts[input] += [n]
            else:
                starts[input] = [n]
        shape = Shape(order[n%len(order)])
        x = 3
        y = 4 + top_rock
        while not shape.landed:
            x, y = shape.move(inputs[input%len(inputs)], x, y,field)
            x, y = shape.move('v', x, y, field)
            input += 1
        for i in range(4):
            for j in range (4):
                if shape.space[i][j] == 1:
                    field[i+y][j+x] = 1
                    top_rock = max(top_rock, i+y)
    return (top_rock, starts)

with open('input.txt', 'r') as f:
    line = f.readlines()

inputs = []
for i in range(len(line[0])-1):
    inputs.append(line[0][i])

print(inputs)
order = ['horizontal','cross','L','vertical','square']

print(run(2022)[0]) #3175