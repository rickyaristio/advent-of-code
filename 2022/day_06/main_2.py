def commonCharacters(group) :
    MAX_CHAR = 26
    prim = [False] * MAX_CHAR

    for i in range(len(group)):
        prim[ord(group[i]) - ord('a')] = True
            
    number = sum(prim)

    return number


with open('input.txt', 'r') as f:
    lines = f.readlines()

print(len(lines[0]))

chars = []

for i in range (14):
    chars.append(lines[0][i])

# print(chars)
value = 0

for i in range(14,int(len(lines[0]))):

    number = commonCharacters(chars)

    if(number == 14):
        value = i 
        break

    chars.pop(0)
    chars.append(lines[0][i])

print(value) #3605


