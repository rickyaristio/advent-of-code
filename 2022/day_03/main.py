with open('input.txt', 'r') as f:
    lines = f.readlines()
    list = [entry.strip() for entry in lines]

# task 1

first_compartment = []
second_compartment = []
result = []
result_value = []

for line in list:
    firstpart, secondpart = line[:int(len(line)/2)], line[int(len(line)/2):]
    first_compartment.append(firstpart)
    second_compartment.append(secondpart)

    for i in firstpart:
        if(i in secondpart):
            if i.isupper() == True:
                result_value.append(ord(i) - 64 + 26)
            else:
                result_value.append(ord(i) - 96)
            break

print(sum(result_value)) #8298
