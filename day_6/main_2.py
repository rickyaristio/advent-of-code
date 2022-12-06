with open('input.txt', 'r') as f:
    lines = f.readlines()

print(len(lines[0]))

char_1 = lines[0][0]
char_2 = lines[0][1]
char_3 = lines[0][2]
char_4 = lines[0][3]
char_5 = lines[0][4]
char_6 = lines[0][5]
char_7 = lines[0][6]
char_8 = lines[0][7]
char_9 = lines[0][8]
char_10 = lines[0][9]
char_11 = lines[0][10]
char_12 = lines[0][11]
char_13 = lines[0][12]
char_14 = lines[0][13]
temp = ""
value = 0

for i in range(14,int(len(lines[0]))):

    temp = lines[0][i]
    char_1 = char_2
    char_2 = char_3
    char_3 = char_4
    char_4 = char_5
    char_5 = char_6
    char_6 = char_7
    char_7 = char_8
    char_8 = char_9
    char_9 = char_10
    char_11 = char_10
    char_12 = char_11
    char_13 = char_12
    char_14 = temp

    print(i)
    
    if(char_1 == char_14 or char_2 == char_13 or char_3 == char_12 or char_4 == char_11 or char_5 == char_10 or char_6 == char_9 or char_7 == char_8):
        continue
    elif(char_1 == char_6 or char_2 == char_5 or char_3 == char_4):
        continue
    elif(char_1 == char_2 or char_3 == char_7):
        continue
    elif(char_1 == char_3):
        continue
    else:
        value = i + 1
        break


print(value) #1275
print(char_1)
print(char_2)
print(char_3)
print(char_4)
print(char_5)
print(char_6)
print(char_7)
print(char_8)
print(char_9)
print(char_10)
print(char_11)
print(char_12)
print(char_13)
print(char_14)

