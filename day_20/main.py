import numpy as np


with open('input.txt', 'r') as f:
    lines = f.readlines()

initial_array = []
dummy_array = []

for line in lines:
    initial_array.append(int(line))

num_array = len(initial_array)
print(initial_array,num_array)

dummy_array = initial_array
for item in initial_array:
    # initial_array.remove(item)
    # initial_array.insert(new_index, item)