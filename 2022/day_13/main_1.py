def compareList(list_left,list_right):
    for n in range(max(len(list_left),len(list_right))):

        if n == min(len(list_left),len(list_right)):
            if(len(list_left) < len(list_right)):
                list_left.append(0)
            elif(len(list_left) > len(list_right)):
                list_right.append(0)

        # integer vs integer
        if(isinstance(list_left[n], int)  == True and isinstance(list_right[n], int)  == True):
            if list_left[n] > list_right[n]:
                return 1
            elif list_left[n] < list_right[n]:
                return 0 
            else:
                continue
        # integer vs list
        elif(isinstance(list_left[n], int)  == True):
            list_left_temp = [list_left[n]]
            if compareList(list_left_temp,list_right[n]) == 1:
                return 1
            elif compareList(list_left_temp,list_right[n]) == 0:
                return 0 
        # list vs integer
        elif(isinstance(list_right[n], int)  == True):
            list_right_temp = [list_right[n]]
            if compareList(list_left[n],list_right_temp) == 1:
                return 1
            elif compareList(list_left[n],list_right_temp) == 0:
                return 0 
        # list vs list
        else:
            if compareList(list_left[n],list_right[n]) == 1:
                return 1
            elif compareList(list_left[n],list_right[n]) == 0:
                return 0 

with open('input.txt', 'r') as f:
    lines = f.readlines()

list_left = []
list_right = []
pairs = []
for n in range(int((len(lines)+1)/3)):

    list_left = eval(lines[n*3])
    list_right = eval(lines[n*3+1])
    
    score = compareList(list_left,list_right)
    if score == 0:
        pairs.append(n+1)


print(pairs)
print(sum(pairs)) #6086




