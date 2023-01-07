def removeEmptySting(test_list):
    while(" " in test_list):
        test_list.remove(" ")
    return test_list

def moveStacks(number,list_from, list_to):
    limit = len(list_from)-1
    for i in range(number):
        list_to.append(list_from[-1])
        list_from.pop()
        if(i == limit):
            break
    return list_from, list_to

with open('input.txt', 'r') as f:
    lines = f.readlines()

crate_1 = []
crate_2 = []
crate_3 = [] 
crate_4 = []
crate_5 = []
crate_6 = []
crate_7 = []
crate_8 = []
crate_9 = []

for i in range(8):
    crate_1.insert(0, lines[i][1])
    crate_2.insert(0, lines[i][5])
    crate_3.insert(0, lines[i][9])
    crate_4.insert(0, lines[i][13])
    crate_5.insert(0, lines[i][17])
    crate_6.insert(0, lines[i][21])
    crate_7.insert(0, lines[i][25])
    crate_8.insert(0, lines[i][29])
    crate_9.insert(0, lines[i][33])

crate_1 = removeEmptySting(crate_1)
crate_2 = removeEmptySting(crate_2)
crate_3 = removeEmptySting(crate_3)
crate_4 = removeEmptySting(crate_4)
crate_5 = removeEmptySting(crate_5)
crate_6 = removeEmptySting(crate_6)
crate_7 = removeEmptySting(crate_7)
crate_8 = removeEmptySting(crate_8)
crate_9 = removeEmptySting(crate_9)

crates = [crate_1, crate_2, crate_3, crate_4, crate_5, crate_6, crate_7, crate_8, crate_9]

for i in range (10,int(len(lines))):
    split = lines[i].split(" ")
    input_1 = int(split[1])
    input_2 = int(split[3])-1
    input_3 = int(split[5])-1

    crates[input_2],crates[input_3] = moveStacks(input_1,crates[input_2],crates[input_3])
    
result = ""
for crate in crates:
    result+=str(crate[-1])

print(result) #WSFTMRHPP






