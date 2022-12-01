with open('input.txt', 'r') as f:
    lines = f.readlines()
    
#näive solution

calories = []
temp = 0
for entry in lines:
    if not entry.isspace():
        temp += int(entry.strip())
    else:
        calories.append(temp)
        temp = 0

#task 1
highest_calories = max(calories)
print(highest_calories) #70509

#task 2
sorted_calories = sorted(calories)
total_highest_calories = highest_calories + sorted_calories[-2] + sorted_calories[-3]
print(total_highest_calories) #208567
