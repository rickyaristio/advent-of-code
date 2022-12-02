with open('input.txt', 'r') as f:
    lines = f.readlines()
    list = [entry.strip() for entry in lines]
   
#very näive solution

first_column = []
second_column = []

for line in list:
    split = line.split(" ") 
    if split[0] == 'A':
        value_1 = 1
    elif split[0] == 'B':
        value_1 = 2
    elif split[0] == 'C':
        value_1 = 3
    
    if split[1] == 'X':
        value_2 = 1
    elif split[1] == 'Y':
        value_2 = 2
    elif split[1] == 'Z':
        value_2 = 3

    first_column.append(value_1)
    second_column.append(value_2)

# task 1
score_1 = 0
for i in range(len(first_column)):
    score_1 += second_column[i]
    if first_column[i] == second_column[i]:
        score_1 += 3
    if (first_column[i] == 1 and second_column[i] == 2) or (first_column[i] == 2 and second_column[i] == 3) or (first_column[i] == 3 and second_column[i] == 1):
        score_1 += 6

print(score_1) #13682

# task 2
score_2 = 0
for i in range(len(first_column)):
    if second_column[i] == 2:
        score_2 += 3 + first_column[i]
    if second_column[i] == 1:
        if first_column[i] == 1:
            score_2 += 0 + 3
        elif first_column[i] == 2:
            score_2 += 0 + 1
        elif first_column[i] == 3:
            score_2 += 0 + 2
    if second_column[i] == 3:
        if first_column[i] == 1:
            score_2 += 6 + 2
        elif first_column[i] == 2:
            score_2 += 6 + 3
        elif first_column[i] == 3:
            score_2 += 6 + 1

print(score_2) #12881

