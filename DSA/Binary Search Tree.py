class Node(object):
    def __init__(self, data):
        self.data = data
        self.leftChild, self.rightChild = None, None

class BinarySearchTree(object):
    def __init__(self):
        self.rootNode = None

    def insert(self, data):
        self.insert_node(data, self.rootNode)

    def insert_node(self, data, node):
        if self.rootNode is None:
            self.rootNode = Node(data)
        else:
            if data < node.data:
                if node.leftChild is not None:
                    self.insert_node(data, node.leftChild)
                else:
                    node.leftChild = Node(data)
            else:
                if node.rightChild is not None:
                    self.insert_node(data, node.rightChild)
                else:
                    node.rightChild = Node(data)

    def traverse(self):
        if self.rootNode:
            self.traverseInOrder(self.rootNode)

    def traverseInOrder(self, root):
        if root is None:
            return
        self.traverseInOrder(root.leftChild)
        print(root.data)
        self.traverseInOrder(root.rightChild)

    def getMaxValue(self):
        if self.rootNode:
            return self.getMax(self.rootNode)

    def getMax(self, node):
        if node.rightChild:
            return self.getMax(node.rightChild)
        return node.data

    def searchNode(self, data):
        if self.rootNode is None:
            return "Empty Binary Tree"
        return self.search(data, self.rootNode)

    def search(self, data, node):
        if node is None:
            return "Not found"
        if data == node.data:
            return "value found"
        elif data > node.data:
            return self.search(data, node.rightChild)
        else:
            return self.search(data, node.leftChild)


bst = BinarySearchTree()
bst.insert(10)
bst.insert(4)
bst.insert(5)
bst.insert(100)
bst.insert(-2)
bst.insert(34)
bst.insert(25)

bst.traverse()

print(bst.getMaxValue())

print(bst.searchNode(-3))










x, y, z = 9, 5, 4
z = (z^x)^y
y = y^x
x = x^3
print(x+y+z)