class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList(object):
    def __init__(self):
        self.head = None

    def insert(self, data):
        if self.head is None:
            self.head = Node(data)
        else:
            currentNode = self.head
            while currentNode.next is not None:
                currentNode = currentNode.next
            currentNode.next = Node(data)

    def insert_at_beginning(self, data):
        if self.head is None:
            self.head = Node(data)
        else:
            newNode = Node(data)
            newNode.next = self.head
            self.head = newNode

    def show_linkedList(self):
        currentNode = self.head
        while currentNode is not None:
            print(f"|{currentNode.data}|->", end=" ")
            currentNode = currentNode.next
        print("NULL")

    def reverse_linkedList(self):
        currentPointer = self.head
        previousPointer = None
        while currentPointer is not None:
            nextPointer = currentPointer.next
            currentPointer.next = previousPointer
            previousPointer = currentPointer
            currentPointer = nextPointer
        self.head = previousPointer
        self.show_linkedList()

    def remove_node(self, data):
        if self.head.data == data:
            self.head = self.head.next
        else:
            previousPointer = None
            currentPointer = self.head
            # nextPointer = self.head.next
            while currentPointer is not None:
                if currentPointer.data == data:
                    previousPointer.next = currentPointer.next
                previousPointer = currentPointer
                currentPointer = currentPointer.next
        self.show_linkedList()

    def find_middle(self):
        small = self.head
        large = self.head
        while True:
            if large is None or large.next is None:
                print(small.data)
                break
            small = small.next
            large = large.next.next

    def partial_reverse(self, m, n):
        global startNode
        currentNode = self.head
        counter = 1
        listSoFar = LinkedList()
        while True:
            if counter == m-1:
                startNode = currentNode
            if n >= counter >= m:
                if listSoFar.head is None:
                    listSoFar.head = Node(currentNode.data)
                else:
                    listSoFar.insert_at_beginning(currentNode.data)
            if counter == n+1:
                endNode = currentNode
                startNode.next = listSoFar.head
                temp = listSoFar.head
                while temp.next is not None:
                    temp = temp.next
                temp.next = endNode
                break
            currentNode = currentNode.next
            counter += 1
        self.show_linkedList()

if __name__ == "__main__":
    ll = LinkedList()
    ll.insert(2)
    ll.insert(5)
    ll.insert(8)
    ll.insert(10)
    ll.insert(22)
    ll.insert(25)
    ll.insert(30)
    ll.insert(45)
    ll.insert(450)
    ll.insert(-72)
    ll.show_linkedList()
    ll.find_middle()
    ll.insert_at_beginning(100)
    ll.show_linkedList()
    ll.partial_reverse(2, 11)

