def recursion(equations, root):
    val = equations[root]
    if type(val) == type(int()):
        return val
    if val == '?':
        return val
    
    left_op = recursion(equations, val[0])
    right_op = recursion(equations, val[2])

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
        if left_op == '?':
            equations[root][2] = right_op
        else:
            equations[root][0] = left_op
        return '?'

with open('input.txt', 'r') as f:
    lines = f.readlines()

equations = {}

for line in lines:
    split_line = line.split()
    if len(split_line) > 2:
        equations[split_line[0][:-1]] = (split_line[1:])
    else:
        equations[split_line[0][:-1]] = int(split_line[1])

print(equations)

total = recursion(equations,'root')
print(total) #51928383302238
