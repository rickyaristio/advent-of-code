#credits: https://www.reddit.com/r/adventofcode/comments/zt6xz5/comment/j1damar/?utm_source=share&utm_medium=web2x&context=3


with open('input.txt', 'r') as f:
    line = f.read().splitlines()

directions = {'N': [(-1,-1),( 0,-1),( 1,-1)],
              'S': [(-1, 1),( 0, 1),( 1, 1)],
              'W': [(-1, 1),(-1, 0),(-1,-1)],
              'E': [( 1, 1),( 1, 0), (1,-1)]}

order = ['N','S','W','E']

list_of_elves = []
positions = set()
for j in range(len(line)):
    for i in range(len(line[0])):
        if line[j][i] == '#':
            list_of_elves.append([(i,j),(i,j)])
            positions |= {(i,j)}

for n in range(10000):
    move = False
    blocklist = set()
    proposals = set()

    for elf in list_of_elves:
        p = elf[0]
        # check if no neighbour
        if all([all([(p[0]+directions[d][i][0],p[1]+directions[d][i][1]) not in positions for i in range(3)]) for d in order]):
            continue
        for d in order:
            if all([(p[0]+directions[d][i][0],p[1]+directions[d][i][1]) not in positions for i in range(3)]):
                proposal = (p[0] + directions[d][1][0],p[1] + directions[d][1][1])
                if proposal in proposals:
                    blocklist |= {proposal}
                else:
                    proposals |= {proposal}
                    elf[1] = proposal
                move = True
                break

    for elf in list_of_elves:
        if elf[1] not in blocklist:
            elf[0] = elf[1] #move to proposal
        else:
            elf[1] = elf[0] #reset proposal to position
    
    order = order[1:] + [order[0]]
    positions = {elf[0] for elf in list_of_elves}

    if n == 9:
        x = {elf[0][0] for elf in list_of_elves}
        y = {elf[0][1] for elf in list_of_elves}
        area = (max(y)-min(y)+1)*(max(x)-min(x)+1)-len(positions)
        
        #task 1
        print(area) #4146
    
    if not move: break

#task 2
print(n+1) #957