import numpy as np
np.set_printoptions(linewidth=np.inf)

def mergeIntervals(intervals):
    #sort intervals
    intervals.sort()
    stack = []
    stack.append(intervals[0])
    for i in intervals[1:]:
        if stack[-1][0] <= i[0] <= stack[-1][-1]:
            stack[-1][-1] = max(stack[-1][-1], i[-1])
        else:
            stack.append(i)
    
    return stack

def checkFuntion(size,list_sensor_x,list_sensor_y,list_beacon_x,list_beacon_y,lines):
    for i in range(size +1):
        print(i)
        coor_y = i
        coor_x = 0
        intervals = []
        # list_coor=np.zeros(size+1)
        for n in range(len(lines)):
            distance = abs(list_sensor_y[n]-list_beacon_y[n])+abs(list_sensor_x[n]-list_beacon_x[n])

            if((coor_y >= list_sensor_y[n] and list_sensor_y[n] + distance >= coor_y) or (list_sensor_y[n]-distance <= coor_y and coor_y <= list_sensor_y[n])):
                distance_y = abs(coor_y-list_sensor_y[n])
                number_x = distance - distance_y

                intervals.append([max(list_sensor_x[n]-number_x,0),(min(list_sensor_x[n]+number_x,size))])
            else:
                continue
        # print(intervals)

        #merge interval
        stack = []
        stack = mergeIntervals(intervals)
        # print(stack)

        if len(stack) == 2:
            coor_x = stack[1][0]-1
            return i,coor_x


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

size = 4000000 #4000000
i,coor_x = checkFuntion(size,list_sensor_x,list_sensor_y,list_beacon_x,list_beacon_y,lines)
            
print(i,coor_x) #2601918 2895970
print(coor_x*size+i) #11583882601918