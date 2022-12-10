import numpy as np

def score20(cycle,score,store_value):
    if(cycle == 20):
        store_value.append(score*20)
    elif(cycle == 60):
        store_value.append(score*60)
    elif(cycle == 100):
        store_value.append(score*100)
    elif(cycle == 140):
        store_value.append(score*140)
    elif(cycle == 180):
        store_value.append(score*180)
    elif(cycle == 220):
        store_value.append(score*220)

with open('input.txt', 'r') as f:
    lines = f.readlines()

cycle = 1
store_value = []
score = 1

for line in lines:
    split = line.split()
    instructions = split[0]

    if instructions == 'noop':
        cycle +=1
        score20(cycle,score,store_value)
    elif instructions == "addx":
        value = int(split[1])
        cycle +=1
        score20(cycle,score,store_value)
        cycle +=1
        score += value
        score20(cycle,score,store_value)
    
print(store_value) 
print(sum(store_value)) #14520
