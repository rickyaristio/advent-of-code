def compareList(list_left,list_right):
    for n in range(max(len(list_left),len(list_right))):

        if n == min(len(list_left),len(list_right)):
            if(len(list_left) < len(list_right)):
                list_left.append(0)
            elif(len(list_left) > len(list_right)):
                list_right.append(0)
        
        # print(n, len(list_left), list_left, list_left[n])
        # print(n, len(list_right), list_right, list_right[n])

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

def sortLists(lists):
    for i in range(1,len(lists)):
        temp = lists[i]
        j = i -1

        #compare temp with the next array
        while j >= 0 and compareList(lists[j],temp):
            lists[j+1] = lists[j]
            j -= 1
        
        lists[j+1] = temp
    return(lists)

with open('input.txt', 'r') as f:
    lines = f.readlines()

lists = []
for n in range(int((len(lines)+1)/3)):

    lists.append(eval(lines[n*3]))
    lists.append(eval(lines[n*3+1]))

lists = sortLists(lists)

#insert [[2]]
pos_2 = 0
lists.append([[2]])
temp = lists[len(lists)-1]
j = len(lists) -2
while j >= 0 and compareList(lists[j],temp):
    lists[j+1] = lists[j]
    j -= 1
    pos_2 += 1
lists[j+1] = temp

#insert [[6]]
pos_6 = 0
lists.append([[6]])
temp = lists[len(lists)-1]
j = len(lists) -2
while j >= 0 and compareList(lists[j],temp):
    lists[j+1] = lists[j]
    j -= 1
    pos_6 += 1
lists[j+1] = temp

# print(lists)
print(len(lists)-pos_2 - 1)
print(len(lists)-pos_6)
print((len(lists)-pos_2 - 1)*(len(lists)-pos_6))