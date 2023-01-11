#kudos: https://github.com/DavidNicolae/AdventOfCode/blob/main/Advent%202022/


def recursion(equations, root,path):
    val = equations[root]
    if type(val) == type(int()):
        return val
    if val == '?':
        path.insert(0,root)
        return val
    
    left_op = recursion(equations, val[0],path)
    right_op = recursion(equations, val[2],path)

    if val[1] == '=':
        return calculate(equations, left_op, right_op, path)

    if left_op != '?' and right_op != '?':
        if val[1] == '+':
            return left_op + right_op
        elif val[1] == '-':
            return left_op - right_op
        elif val[1] == '*':
            return left_op * right_op
        elif val[1] == '/':
            return left_op // right_op
    else:
        path.insert(0,root)
        if left_op == '?':
            equations[root][2] = right_op
        else:
            equations[root][0] = left_op
        return '?'

def calculate(equations,left_op,right_op,path):
    total = right_op
    if left_op != '?':
        total = left_op
    for index,equation in enumerate(path[:-1]):
        temp = equations[equation]
        known_index = 0
        if type(temp[0]) != type(int()):
            known_index = 2
        known_equation = temp[known_index]
        if temp[1] == '+':
            total -= known_equation
        elif temp[1] == '-':
            if known_index == 0:
                total = known_equation - total
            else:
                total += known_equation
        elif temp[1] == '*':
            total = total // known_equation
        elif temp[1] == '/':
            if known_index == 0:
                total = known_equation // total
            else:
                total *= known_equation
    return total


with open('input.txt', 'r') as f:
    lines = f.readlines()

equations = {}

for line in lines:
    split_line = line.split()
    if len(split_line) > 2:
        equations[split_line[0][:-1]] = (split_line[1:])
    else:
        equations[split_line[0][:-1]] = int(split_line[1])

#part 2 (reverse calculation in recursion)
equations['root'][1] = '='
equations['humn'] = '?'
total = recursion(equations,'root',[])
print(total) #3305669217840
