with open('input.txt', 'r') as f:
    lines = f.readlines()
    list = [entry.strip() for entry in lines]

#task 1
horizontal = 0
vertical = 0
for line in lines:
    if line.split()[0] == 'down':
       vertical += int(line.split()[1])
    elif line.split()[0] == 'up':
       vertical -= int(line.split()[1]) 
    elif line.split()[0] == 'forward':
       horizontal += int(line.split()[1])    

print(vertical*horizontal) #1989265

#task 2
forward = 0
depth = 0
aim = 0
for line in lines:
    if line.split()[0] == 'down':
       aim += int(line.split()[1])
    elif line.split()[0] == 'up':
       aim -= int(line.split()[1]) 
    elif line.split()[0] == 'forward':
        depth += int(line.split()[1]) * aim
        forward += int(line.split()[1])
        

print(forward*depth) #2089174012

