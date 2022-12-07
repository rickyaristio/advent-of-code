class Tree():
    def __init__(self,root):
        self.root = root
        self.root_value = 0
        self.children = []
        self.Nodes = []
        self.Nodes_values = []
    def addNode(self,obj):
        self.children.append(obj)
    def getAllNodes(self):
        self.Nodes.append(self.root)
        for child in self.children:
            self.Nodes.append(child.data)
        for child in self.children:
            if child.getChildNodes(self.Nodes) != None:
                child.getChildNodes(self.Nodes)
    def getAllNodesValues(self):
        for child in self.children:
            child.updateChildValues()
            self.root_value += child.data_value
            self.Nodes_values.append(child.data_value)
        for child in self.children:
            if child.getChildNodesValues(self.Nodes_values) != None:
                child.getChildNodesValues(self.Nodes_values)
        self.Nodes_values.insert(0, self.root_value)


class Node():
    def __init__(self,data):
        self.data = data
        self.data_value = 0
        self.children = []
    def addNode(self,obj):
        self.children.append(obj)
    def addValue(self,val):
        self.data_value += val
    def getChildNodes(self,Tree):
        for child in self.children:
            if child.children:
                child.getChildNodes(Tree)
                Tree.append(child.data)
            else:
                Tree.append(child.data)
    def updateChildValues(self):
        for child in self.children:
            if child.children:
                self.data_value += child.data_value
                child.updateChildValues()
            else:
                self.data_value += child.data_value
    def getChildNodesValues(self,Tree):
        for child in self.children:
            if child.children:
                self.data_value += child.data_value
                child.getChildNodesValues(Tree)
                Tree.append(child.data_value)
            else:
                self.data_value += child.data_value
                Tree.append(child.data_value)




FunCorp =  Tree('A')
FunCorp.addNode(Node('B1'))
FunCorp.addNode(Node('B2'))
FunCorp.addNode(Node('B3'))
FunCorp.children[0].addNode(Node('C1'))
FunCorp.children[1].addNode(Node('C2'))
FunCorp.children[0].children[0].addNode(Node('D1'))
FunCorp.children[0].children[0].addValue(2)
FunCorp.children[0].children[0].children[0].addValue(3)

# FunCorp.children[0].children[0].children[0].addNode(Node('E1',8))

print()

FunCorp.getAllNodes()
FunCorp.getAllNodesValues()
# FunCorp.getAllSumValues()

print(FunCorp.Nodes)
print(FunCorp.Nodes_values)
# print(FunCorp.Nodes_sum_value)









class Tree():
    def __init__(self,root):
        self.data = root
        self.value = 0
        self.child = {}
    def append(self,title,child,value_child):
        self.child[title] = child
        self.value += value_child


# root = Node('root')
# print(root.value)

# child = Node('child')
# print(child.data)

# root.append('child_1',child,child.value)
# print(root.value)

# grand_child_1 = Node('grand_child_1')
# print(grand_child_1.data)

# grand_child_2 = Node('grand_child_2')
# print(grand_child_2.data)

# child.append('grand_child_1',grand_child_1,2)
# print(child.value)

# child.append('grand_child_2',grand_child_2,5)
# print(child.value)

# print(root.value)

with open('input.txt', 'r') as f:
    lines = f.readlines()


# for i in range(int(len(lines))):
#     split = lines[i].split(" ")
    
#     if(split[1] == 'cd'):
#         if(split[2] == '/'):
#             root = Node('root')
#         elif(split[2] == '..'):
#             pass
    
#     elif(split[1] == 'ls'):
#         pass

#     elif(split[0] == 'dir'):
#         pass
    
#     elif(type(split[0]) == int):
#         pass


print(len(lines))




