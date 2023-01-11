import numpy as np

def updatePosition(sprite_position,sprite_pointer,score):
    sprite_position = [0] * 40

    a = (sprite_pointer-1+score) % 40
    b = (sprite_pointer+score) % 40
    c = (sprite_pointer+1+score) % 40
 
    sprite_position[a] = 1
    sprite_position[b] = 1
    sprite_position[c] = 1
    return sprite_position

def updateCRT(sprite_position,store_CRT,cycle):
    if sprite_position[cycle] == 1:
        store_CRT.append(1)
    else:
        store_CRT.append(0)


with open('input.txt', 'r') as f:
    lines = f.readlines()

cycle = 1
score = 1
store_CRT = []
convert_CRT = []

sprite_position = [0] * 40
sprite_pointer = 0
sprite_position[0] = sprite_position[1] = sprite_position[2] = 1


for line in lines:
    split = line.split()
    instructions = split[0]

    if instructions == 'noop':
        updateCRT(sprite_position,store_CRT,cycle-1)
        cycle +=1
        if(cycle == 41):
            cycle = 1
    elif instructions == "addx":
        value = int(split[1])
    
        updateCRT(sprite_position,store_CRT,cycle-1)
        cycle +=1
        if(cycle == 41):
            cycle = 1
        updateCRT(sprite_position,store_CRT,cycle-1)
        score += value
        sprite_position = updatePosition(sprite_position,sprite_pointer,score)
        cycle +=1
        if(cycle == 41):
            cycle = 1
        
for i in range(len(store_CRT)) :
    if(store_CRT[i] == 1):
        convert_CRT.append('#')
    else:
        convert_CRT.append(".")

# print(store_CRT) 
print(''.join(map(str, convert_CRT[0:40])))
print(''.join(map(str, convert_CRT[40:80])))
print(''.join(map(str, convert_CRT[80:120])))
print(''.join(map(str, convert_CRT[120:160])))
print(''.join(map(str, convert_CRT[160:200])))
print(''.join(map(str, convert_CRT[200:240])))



