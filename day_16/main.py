import numpy as np
import itertools
np.set_printoptions(linewidth=np.inf)

#find path (recursive)
# def findPath(graph,start,end,path=[]):
#     path = path + [start]
#     if start == end:
#         return path
#     for node in graph[start]:
#         if node not in path:
#             rec_path = findPath(graph,node,end,path)
#             if rec_path:
#                 return rec_path

# def findAllPath(graph,start,end,path=[]):
#     path = path + [start]
#     if start == end:
#         return [path]
#     paths = []
#     for node in graph[start]:
#         if node not in path:
#             rec_paths = findAllPath(graph,node,end,path)
#             for rec_path in rec_paths:
#                 paths.append(rec_path)
#     return paths

def findShortestPath(graph,start,end,path=[]):
    path = path + [start]
    if start == end:
        return path
    shortest = None
    for node in graph[start]:
        if node not in path:
            rec_path = findShortestPath(graph,node,end,path)
            if rec_path:
                if (not shortest) or (len(rec_path) < len(shortest)):
                    shortest = rec_path
    return shortest

def permutFunc(myList):
	if len(myList) == 0:
		return []
	if len(myList) == 1:
		return [myList]

	k = []
	for i in range(len(myList)):
		m = myList[i]
		res = myList[:i] + myList[i+1:]
		for p in permutFunc(res):
			k.append([m] + p)
	return k


with open('input.txt', 'r') as f:
    lines = f.readlines()


checked = []
graph = {}

for line in lines:
    split_line = line.split()

    if(int(split_line[4].split('=')[1].split(';')[0])):
        checked.append([split_line[1],int(split_line[4].split('=')[1].split(';')[0])])

    graph[split_line[1]] = []
    for i in range(9,len(split_line)):
            graph[split_line[1]].append(split_line[i].split(',')[0])
        
    
# print(graph)
print(checked)

# print(findPath(graph,'EE','AA'))
# print(findAllPath(graph,'EE','AA'))
# print(findShortestPath(graph,'AA','DD'),len(findShortestPath(graph,'AA','DD')))

highest = 0
for p in permutFunc(checked):
    p.insert(0,['AA',0])
    distance = 30
    temp = 0
    for i in range(len(p)-1):
        if distance < 0:
            break
        distance -= len(findShortestPath(graph,p[i][0],p[i+1][0]))
        temp += distance*p[i+1][1]
    if(temp > highest):
        highest = temp


# for p in itertools.permutations(checked):
#     # p.insert(0,['AA',0])
#     print('yo')
#     distance = 30-len(findShortestPath(graph,'AA',p[0][0]))
#     temp = distance*p[0][1]
#     for i in range(len(p)-1):
#         if distance < 0:
#             break
#         distance -= len(findShortestPath(graph,p[i][0],p[i+1][0]))
#         temp += distance*p[i+1][1]
#     if(temp > highest):
#         highest = temp
print(highest)

