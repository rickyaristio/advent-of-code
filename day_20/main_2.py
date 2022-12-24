
number_list = []
decryption_key = 811589153
with open('input.txt', 'r') as f:
    number_list = list(enumerate(map(int, f.read().splitlines())))

for id, val in number_list:
    number_list[id] = (id, val * decryption_key)

# print(number_list)

len_list = len(number_list)

for n in range(10): #mix 10x
    for i in range(len_list): 
        for j in range(len_list):
            if number_list[j][0] == i:
                num = number_list[j]
                number_list.pop(j)
                if num[1] == -j:
                    number_list.append(num)
                else:
                    number_list.insert((j + num[1]) % (len_list-1), num)
                break

index_zero = 0
for i in range(len_list): 
    if number_list[i][1] == 0:
        index_zero = i
        break

index_1000 = number_list[(1000+index_zero) % len_list][1]
index_2000 = number_list[(2000+index_zero) % len_list][1]
index_3000 = number_list[(3000+index_zero) % len_list][1]
sum = index_1000 + index_2000 + index_3000

print(sum) #535648840980
