import numpy as np
np.set_printoptions(linewidth=np.inf)



with open('input.txt', 'r') as f:
    lines = f.readlines()

sources = []
receivers = []
flow_rates = []

for line in lines:
    split_line = line.split()
    sources.append(split_line[1])
    flow_rates.append(int(split_line[4].split('=')[1].split(';')[0]))
    receiver = []
    for i in range(9,len(split_line)):
        if i == range(len(line)-1):
            receiver.append(split_line[i])
        else:
            receiver.append(split_line[i].split(',')[0])
        
    receivers.append(receiver)
    

print(sources)
print(receivers)
print(flow_rates)
