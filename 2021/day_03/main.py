with open('input.txt', 'r') as f:
    lines = f.readlines()
    list = [entry.strip() for entry in lines]

#task 1
gamma_rate = 0
epsilon_rate = 0

for i in range(len(lines[0])-1):
   sum = 0
   for line in lines:
      sum += int(line[len(lines[0])-2-i])
   if(sum*2 > len(lines)):
      gamma_rate += pow(2,i)
   else:
      epsilon_rate += pow(2,i)

print(gamma_rate,epsilon_rate,gamma_rate*epsilon_rate) #654 3441 2250414
