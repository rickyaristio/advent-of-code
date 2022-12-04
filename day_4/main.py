with open('input.txt', 'r') as f:
    lines = f.readlines()

count = 0
for line in lines:
    split = line.split(",")
    elf_1 = split[0]
    elf_2 = split[1]   
    split_1 = elf_1.split("-")
    split_2 = elf_2.split("-")
    elf_1_min = int(split_1[0])
    elf_1_max = int(split_1[1])
    elf_2_min = int(split_2[0])
    elf_2_max = int(split_2[1])

    if(elf_1_min <= elf_2_min and elf_1_max >= elf_2_max):
        count +=1
    elif(elf_2_min <= elf_1_min and elf_2_max >= elf_1_max):
        count +=1

print(count) #540






