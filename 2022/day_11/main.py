class Monkey():
    def __init__(self,id,items,operation_1,operation_2,test,if_true,if_false):
        self.id = id
        self.items = items
        self.operation_1 = operation_1
        self.operation_2 = operation_2
        self.test = test
        self.if_true = if_true
        self.if_false = if_false

with open('input.txt', 'r') as f:
    lines = f.readlines()

monkeys = []
for n in range(int((len(lines)+1)/7)):
    id = n
    items = []
    for i in range(2,len(lines[(n*7)+1].split())):
        items.append(int(lines[(n*7)+1].replace(',','').split()[i]))
    operation_1 = lines[(n*7)+2].split()[4]
    operation_2 = lines[(n*7)+2].split()[5]
    test = int(lines[(n*7)+3].split()[3])
    if_true = int(lines[(n*7)+4].split()[5])
    if_false = int(lines[(n*7)+5].split()[5])

    monkey = Monkey(id,items,operation_1,operation_2,test,if_true,if_false)
    monkeys.append(monkey)

inspected_items = [0] * len(monkeys)
for m in range(20):
    for n in range(len(monkeys)):
        for item in monkeys[n].items:
            if monkeys[n].operation_1 == '*':
                if monkeys[n].operation_2 == 'old':
                    item *= item
                else:
                    item *= int(monkeys[n].operation_2)
            elif monkeys[n].operation_1 == '+':
                if monkeys[n].operation_2 == 'old':
                    item += item
                else:
                    item += int(monkeys[n].operation_2)
            
            item /= 3
            if int(item) % monkeys[n].test == 0:
                monkeys[monkeys[n].if_true].items.append(int(item))
            else:
                monkeys[monkeys[n].if_false].items.append(int(item))

            inspected_items[n] += 1

        monkeys[n].items = []

#print(inspected_items)
print(max(inspected_items)*sorted(inspected_items)[-2]) #54752

        




