class Tree():
    def __init__(self,name,size=0):
        self.name = name
        self.size = size
        self.children = []
        self.parent = None

root = Tree('/')
temp = root

with open('input.txt', 'r') as f:
    lines = f.readlines()

for line in lines:
    split = line.split()
    if(split[0] == '$'):
        if(split[1] == 'cd'):
            directory = split[2]
            if directory == '..':
                temp = temp.parent
            else: 
                child = Tree(directory)
                child.parent = temp
                temp.children.append(child)
                temp = child
    else:
        name = split[0]
        if name != 'dir':
            child = Tree(split[1], int(split[0]))
            temp.children.append(child)

sizes = []

def dir_sizes(root):
    if not root.children:
        return root.size
    
    total = 0
    for child in root.children:
        total += dir_sizes(child)
    
    sizes.append(total)
    return total

used = dir_sizes(root)

#task 1
value = 0
for i in range(int(len(sizes))):
    if(sizes[i] < 100000):
        value += sizes[i]

print(value) #1348005

#task 2
disk_available = 70000000
unused_space = 30000000

value_2 = 0
sizes.sort()
print(sizes)
for i in range(int(len(sizes))):
    if((max(sizes) - sizes[i]) < (disk_available - unused_space)):
        value_2 = sizes[i]
        break

print(value_2) #12785886




