import timeit

class Monkey():
    def __init__(self,id,items,operation_1,operation_2,test,if_true,if_false):
        self.id = id
        self.items = items
        self.operation_1 = operation_1
        self.operation_2 = operation_2
        self.test = test
        self.if_true = if_true
        self.if_false = if_false

start = timeit.timeit()

with open('input.txt', 'r') as f:
    lines = f.readlines()

monkeys = []
for n in range(int((len(lines)+1)/7)):
    id = n
    items = []
    for i in range(2,len(lines[(n*7)+1].split())):
        sub_item = []
        sub_item.append([int(lines[(n*7)+1].replace(',','').split()[i]),0])
        items.append(sub_item)
    operation_1 = lines[(n*7)+2].split()[4]
    operation_2 = lines[(n*7)+2].split()[5]
    test = int(lines[(n*7)+3].split()[3])
    if_true = int(lines[(n*7)+4].split()[5])
    if_false = int(lines[(n*7)+5].split()[5])

    monkey = Monkey(id,items,operation_1,operation_2,test,if_true,if_false)
    monkeys.append(monkey)

inspected_items = [0] * len(monkeys)
for m in range(10000):
    print(m)
    for n in range(len(monkeys)):
        for item in monkeys[n].items:
            item.append([monkeys[n].operation_2,monkeys[n].operation_1])

            # function to check mod            
            check_mod = int(item[0][0]) % monkeys[n].test
            for i in range(1,len(item)):
                if item[i][1] == '*':
                    if item[i][0] == 'old':
                        check_mod *= check_mod 
                    else:
                        check_mod *= int(item[i][0]) % monkeys[n].test
                    check_mod = check_mod % monkeys[n].test
                elif item[i][1] == '+':
                    check_mod += int(item[i][0]) % monkeys[n].test 
                    check_mod = check_mod % monkeys[n].test  
            
            if check_mod == 0:
                monkeys[monkeys[n].if_true].items.append(item)
            else:
                monkeys[monkeys[n].if_false].items.append(item)

            inspected_items[n] += 1
        
        monkeys[n].items = []

print(inspected_items) #[60002, 56692, 63353, 116668, 60034, 116628, 60010, 63343]
print(max(inspected_items)*sorted(inspected_items)[-2]) #13606755504

end = timeit.timeit() 
print('time:',end - start,'s') #
## very naive solution! please reconsider it!

        




