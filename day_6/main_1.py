with open('input.txt', 'r') as f:
    lines = f.readlines()

print(len(lines[0]))

char_1 = lines[0][0]
char_2 = lines[0][1]
char_3 = lines[0][2]
char_4 = lines[0][3]
temp = ""
value = 0

for i in range(4,int(len(lines[0]))):

    temp = lines[0][i]
    char_1 = char_2
    char_2 = char_3
    char_3 = char_4
    char_4 = temp
    
    if(char_2 == char_1 or char_3 == char_1 or char_4 == char_1):
        continue
    elif(char_3 == char_2 or char_2 == char_4):
        continue
    elif(char_4 == char_3):
        continue
    else:
        value = i + 1
        break


print(value) #1275
print(char_1)
print(char_2)
print(char_3)
print(char_4)

