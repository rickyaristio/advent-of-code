def compareList(list_left,list_right):
    if(len(list_left) > len(list_right)):
        return 1
    elif(len(list_left) < len(list_right)):
        return 0
    elif(len(list_left) == len(list_right)):
        for n in range(len(list_left)):
            
            if not list_left: #empty list
                list_left.append(0)
            if not list_right:
                list_right.append(0)

            if(isinstance(list_left[n], int)  == True and isinstance(list_right[n], int)  == True):
                if list_left[n] > list_right[n]:
                    return 1
                elif list_left[n] < list_right[n]:
                    return 0 
                else:
                    continue
            elif(isinstance(list_left[n], int)  == True): #integer
                print('debug')
                for m in range(len(list_right[n])):
                    if list_left[n] > list_right[n][m]:
                        return 1
                    elif list_left[n] < list_right[n][m]:
                        return 0
            elif(isinstance(list_right[n], int)  == True):
                for m in range(len(list_left[n])):
                    if list_right[n] > list_left[n][m]:
                        return 0
                    elif list_right[n] < list_left[n][m]:
                        return 1
            else:
                if(len(list_left[n]) == 1 and len(list_right[n]) == 1):
                    if list_left[n][0] > list_right[n][0]:
                        return 1
                    elif list_left[n][0] < list_right[n][0]:
                        return 0
                    else:
                        continue
                else:
                    list_left = list_left[n]
                    list_right = list_right[n]

                    if compareList(list_left,list_right) == 1:
                        return 1
                    elif compareList(list_left,list_right) == 0:
                        return 0 
            

with open('input.txt', 'r') as f:
    lines = f.readlines()

list_left = []
list_right = []
pairs = []
for n in range(int((len(lines)+1)/3)):

    list_left = eval(lines[n*3])
    list_right = eval(lines[n*3+1])

    # print(list_left, len(list_left))
    
    score = compareList(list_left,list_right)
    if score == 0:
        pairs.append(n+1)


print(pairs)
print(sum(pairs))




