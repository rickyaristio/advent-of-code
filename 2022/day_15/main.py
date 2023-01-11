import numpy as np
np.set_printoptions(linewidth=np.inf)


with open('input.txt', 'r') as f:
    lines = f.readlines()

list_sensor_x = []
list_sensor_y = []
list_beacon_x = []
list_beacon_y = []

for line in lines:
    split_line = line.split()
    list_sensor_x.append(int(split_line[2].split('=')[1].split(',')[0]))
    list_sensor_y.append(int(split_line[3].split('=')[1].split(':')[0]))
    list_beacon_x.append(int(split_line[8].split('=')[1].split(',')[0]))
    list_beacon_y.append(int(split_line[9].split('=')[1]))

min_x = min(min(list_sensor_x),min(list_beacon_x))
max_x = max(max(list_sensor_x),max(list_beacon_x))
min_y = min(min(list_sensor_y),min(list_beacon_y))
max_y = max(max(list_sensor_y),max(list_beacon_y))

# print(min_x,max_x,min_y,max_y)

#consider case 1
input_y = 2000000
count = 0
list_coor={}
for n in range(len(lines)):
    distance = abs(list_sensor_y[n]-list_beacon_y[n])+abs(list_sensor_x[n]-list_beacon_x[n])
    # print(distance)
    if((input_y > list_sensor_y[n] and list_sensor_y[n] + distance > input_y) or (list_sensor_y[n]-distance < input_y and input_y < list_sensor_y[n])):
        distance_y = abs(input_y-list_sensor_y[n])
        number_x = distance - distance_y
        # print(n,distance,distance_y,number_x)
        for m in range(2*number_x+1):
            list_coor[list_sensor_x[n]-min_x-number_x+m] = 3
    else:
        continue

# print(list_coor)

for key in list_coor:
    if(list_coor[key] % 2 == 1):
        count += 1
print(count-1) #4985193