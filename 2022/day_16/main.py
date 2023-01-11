#credits: https://github.com/tomfran/advent-of-code/


with open('input.txt', 'r') as f:
    lines = f.readlines()

checked = {}
graph = {}

for line in lines:
    split_line = line.split()

    if(int(split_line[4].split('=')[1].split(';')[0])):
        checked[split_line[1]] = int(split_line[4].split('=')[1].split(';')[0])

    graph[split_line[1]] = []
    for i in range(9,len(split_line)):
        graph[split_line[1]].append(split_line[i].split(',')[0])
    
def bfs(node):
    visited = set([node])
    distance = {}
    q = [node]
    curr_level = 0
    while q:
        next_level = []
        for e in q:
            distance[e] = curr_level
            for adj in graph[e]:
                if adj in visited:
                    continue
                visited.add(adj)
                next_level.append(adj)
        curr_level += 1
        q = next_level
    distance.pop(node)
    return distance
    
min_paths = {}
for node in graph.keys():
    min_paths[node] = bfs(node)

# print(min_paths)

checked_open = {}
ans = 0
answer_space = {}

def normalize(d):
    return tuple(sorted([k for k, v in d.items() if v]))

def update_answer_space(d,v):
    t = answer_space.get(normalize(d),0)
    answer_space[normalize(d)] = max(t,v)

def solve(node, time, curr):
    update_answer_space(checked_open, curr)
    if time <= 0:
        return
    
    checked_open[node] = True
    acc = max(0, checked[node] * (time -1))
    curr += acc

    global ans
    ans = max(ans, curr)

    valves_left = [k for k, v in checked_open.items() if not v]
    if not valves_left:
        update_answer_space(checked_open, curr)
    for left in valves_left:
        time_lost = min_paths[node][left] + 1
        solve(left, time - time_lost, curr)

    checked_open[node] = False

for key in checked.keys():
    checked_open = {}
    for k in checked.keys():
        checked_open[k] = False
    solve(key, 30 - min_paths["AA"][key], 0)
    print(key,ans)

print(checked_open)
print(ans)
    
