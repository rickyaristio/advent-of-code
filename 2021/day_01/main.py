with open('input.txt', 'r') as f:
    lines = f.readlines()
    list = [entry.strip() for entry in lines]

#task 1
count = 0
for i in range(len(lines)-1):
    if int(lines[i+1]) > int(lines[i]):
        count += 1

print(count) #1521

#task 2
count_2 = 0

for i in range(len(lines)-3):
    if int(lines[i+3]) > int(lines[i]):
        count_2 += 1

print(count_2) #1543