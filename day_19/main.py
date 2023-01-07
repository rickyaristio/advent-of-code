#credits: https://github.com/fuglede/adventofcode/blob/master/2022/

from math import inf, prod
import re #regular expression

with open('input.txt', 'r') as f:
    lines = f.read().strip().split("\n")

lists = [list(map(int, re.findall("\d+",x))) for x in lines]


def solve(blueprint, total_time):
    # DFS

    def actions(state):
        time, robots, ores = state
        new_time = time + 1
        time_left = total_time - time

        def new_state(new_robots, new_ores):
            new_ores = [new_ores[i] + robots[i] for i in range(4)]
            #max usage: 4 ore, 20 clay, 20 obsidian
            for i, max_usable in zip(range(3),(4,20,20)):
                ore_max_can_use = max_usable * time_left
                ore_get = robots[i] * (time_left -1)
                new_ores[i] = min(new_ores[i], ore_max_can_use - ore_get)
            return (new_time, tuple(new_robots), tuple(new_ores))

        #build geode robot
        if ores[0] >= blueprint[5] and ores[2] >= blueprint[6]:
            new_ores = list(ores)
            new_ores[0] -= blueprint[5]
            new_ores[2] -= blueprint[6]
            new_robots = list(robots)
            new_robots[3] += 1
            yield new_state(new_robots,new_ores)
            return 

        #build ore robot
        if robots[0] < 4 and ores[0] >= blueprint[1]:
            new_ores = list(ores)
            new_ores[0] -= blueprint[1]
            new_robots = list(robots)
            new_robots[0] += 1
            yield new_state(new_robots,new_ores)

        #build clay robot
        if robots[1] < 20 and ores[0] >= blueprint[2]:
            new_ores = list(ores)
            new_ores[0] -= blueprint[2]
            new_robots = list(robots)
            new_robots[1] += 1
            yield new_state(new_robots,new_ores)

        #build obsidian robot
        if robots[1] < 20 and ores[0] >= blueprint[3] and ores[1] >= blueprint[4]:
            new_ores = list(ores)
            new_ores[0] -= blueprint[3]
            new_ores[1] -= blueprint[4]
            new_robots = list(robots)
            new_robots[2] += 1
            yield new_state(new_robots,new_ores)

        #do nothing 
        yield new_state(robots,ores)

    state = (0, (1,0,0,0),(0,0,0,0)) # (time, robots by type, ores by type)
    seen = set()
    stack = [state]
    best = -inf

    while stack:
        state = stack.pop()
        time, robots, ores = state
        if time == total_time:
            if ores[3] > best:
                best = ores[3]
            continue
        for new_state in actions(state):
            if new_state in seen:
                continue
            seen.add(new_state)
            stack.append(new_state)
    return best

#task 1
sum = 0
for blueprint in lists:
    sum += blueprint[0]*solve(blueprint,24)

print(sum) #1427

#task 2
sum_2 = 1
for blueprint in lists[:3]:
    sum_2 *= solve(blueprint,32)

print(sum_2) #4400