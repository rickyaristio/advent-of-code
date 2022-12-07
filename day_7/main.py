class Tree():
    def __init__(self,root):
        self.root = root
        self.root_value = 0
        self.children = []
        self.Nodes = []
        self.Nodes_values = []
        self.Nodes_sum_value = []
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
        self.Nodes_values.append(self.root_value)
        for child in self.children:
            self.Nodes_values.append(child.data_value)
        for child in self.children:
            if child.getChildNodesValues(self.Nodes_values) != None:
                child.getChildNodesValues(self.Nodes_values)
    def sumValue(self,value):
        for child in self.children:
            value += child.data_value  
        for child in self.children:
            value += child.sumValue(0)             
        return value
    def getAllSumValues(self):
        self.Nodes_sum_value.append(self.sumValue(0))
        for child in self.children:
            self.Nodes_sum_value.append(child.sumValue(0))
        for child in self.children:
            if child.getChildNodesValues(self.Nodes_sum_value) != None:
                child.getChildNodesValues(self.Nodes_sum_value)

class Node():
    def __init__(self,data,val):
        self.data = data
        self.data_value = val
        self.children = []
    def addNode(self,obj):
        self.children.append(obj)
    def getChildNodes(self,Tree):
        for child in self.children:
            if child.children:
                child.getChildNodes(Tree)
                Tree.append(child.data)
            else:
                Tree.append(child.data)
    def getChildNodesValues(self,Tree):
        for child in self.children:
            if child.children:
                child.getChildNodesValues(Tree)
                Tree.append(child.data_value)
            else:
                Tree.append(child.data_value)
    def sumValue(self,value):
        for child in self.children:
            if child.children:
                value += child.sumValue(value)
                value += child.data_value
            else:
                value += child.data_value
        return value
    def getChildSumValues(self,Tree):
        for child in self.children:
            if child.children:
                child.getChildSumValues(Tree)
                Tree.append(child.sumValue(0))
            else:
                Tree.append(child.sumValue(0))
    

FunCorp =  Tree('Head Honcho')
FunCorp.addNode(Node('VP of Stuff',1))
FunCorp.addNode(Node('VP of Shenanigans',2))
FunCorp.addNode(Node('VP of Hootenanny',3))
FunCorp.children[0].addNode(Node('General manager of Fun',4))
FunCorp.children[1].addNode(Node('General manager Shindings',5))
FunCorp.children[0].children[0].addNode(Node('Sub manager of Fun',6))
FunCorp.children[0].children[0].children[0].addNode(Node('Employee of the month',7))
FunCorp.getAllNodes()
FunCorp.getAllNodesValues()
FunCorp.getAllSumValues()

empty_list = []
FunCorp.children[0].getChildNodesValues(empty_list)
print(empty_list)



value = 0
print(FunCorp.sumValue(value))
print(FunCorp.children[0].sumValue(value))
print(FunCorp.children[1].sumValue(value))




print(FunCorp.Nodes)
print(FunCorp.Nodes_values)
print(FunCorp.Nodes_sum_value)


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




