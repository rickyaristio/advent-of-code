def commonCharacters(group) :
    MAX_CHAR = 26
    prim = [True] * MAX_CHAR
    prim_capital = [True] * MAX_CHAR

    for i in range(len(group)):
        sec = [False] * MAX_CHAR
        sec_capital = [False] * MAX_CHAR

        for j in range(len(group[i])):
            if group[i][j].isupper() == True:
                if (prim_capital[ord(group[i][j]) - ord('A')]) :
                    sec_capital[ord(group[i][j]) - ord('A')] = True
            else:
                if (prim[ord(group[i][j]) - ord('a')]) :
                    sec[ord(group[i][j]) - ord('a')] = True

        for k in range(MAX_CHAR):
            prim_capital[k] = sec_capital[k]
            prim[k] = sec[k]
            
    value = 0
    for i in range(26):
        if (prim[i]) :
            value = i + 1
        if (prim_capital[i]) :
            value = i + 27

    return value


with open('input.txt', 'r') as f:
    lines = f.readlines()

group = []
value = 0

for i in range(0,int(len(lines))):
    group.append(lines[i].strip())
    if (i % 3 == 2):
        value += commonCharacters(group)
        group = []

print(value) #2708





