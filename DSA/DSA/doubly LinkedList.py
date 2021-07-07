class Node(object):
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None
        self.child = None

class DoublyLinkedList(object):
    def __init__(self):
        self.head = None

    def insertAtEnd(self, value):
        if self.head is None:
            self.head = Node(value)
        else:
            currentNode = self.head
            while currentNode.next is not None:
                currentNode = currentNode.next
            newNode = Node(value)
            currentNode.next = newNode
            newNode.prev = currentNode

    def traverseList(self):
        if self.head is None:
            print("EMPTY linkedList found !!!")
            return
        currentNode = self.head
        print("NULL <-", end="")
        while currentNode is not None:
            if currentNode.next is None:
                print(f"|{currentNode.data}| ->", end=" ")
                currentNode = currentNode.next
                continue
            print(f"|{currentNode.data}| <->", end=" ")
            currentNode = currentNode.next
        print("NULL")

def MergeMultiLevelDoublyLinkedList(mainHead):
    currentNode = mainHead
    if currentNode is None:
        print("Empty List Found !!!")
        return
    while True:
        if currentNode is None:
            break
        if currentNode.child is None:
            currentNode = currentNode.next
            continue
        else:
            start = currentNode
            end = currentNode.next
            if end is None:
                currentNode.next = currentNode.child
                currentNode.child = None
            else:
                currentInBranch = currentNode.child
                startBranch = currentInBranch
                while currentInBranch.next is not None:
                    currentInBranch = currentInBranch.next
                endBranch = currentInBranch

                start.next = startBranch
                startBranch.prev = start

                endBranch.next = end
                end.prev = endBranch
        currentNode = currentNode.next



if __name__ == "__main__":
    d1 = DoublyLinkedList()
    d1.insertAtEnd(10)
    d1.insertAtEnd(20)
    d1.insertAtEnd(30)
    d1.insertAtEnd(40)
    d1.insertAtEnd(50)
    # d1.traverseList()


    mainBranch = DoublyLinkedList()
    mainBranch.insertAtEnd(1)
    mainBranch.insertAtEnd(2)
    mainBranch.insertAtEnd(3)
    mainBranch.insertAtEnd(4)
    mainBranch.insertAtEnd(5)
    mainBranch.insertAtEnd(6)

    branch1 = DoublyLinkedList()
    branch1.insertAtEnd(7)
    branch1.insertAtEnd(8)
    branch1.insertAtEnd(9)

    branch2 = DoublyLinkedList()
    branch2.insertAtEnd(10)
    branch2.insertAtEnd(11)

    branch3 = DoublyLinkedList()
    branch3.insertAtEnd(12)
    branch3.insertAtEnd(13)

    mainBranch.head.next.child = branch1.head
    branch1.head.next.child = branch2.head
    mainBranch.head.next.next.next.next.child = branch3.head

    mainBranch.traverseList()
    branch1.traverseList()
    branch2.traverseList()
    branch3.traverseList()

    MergeMultiLevelDoublyLinkedList(mainBranch.head)

    mainBranch.traverseList()
