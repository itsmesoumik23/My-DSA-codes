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

    def show_linkedList(self, head):
        head = self.head
        currentNode = head
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
        self.show_linkedList(self.head)

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
        self.show_linkedList(self.head)

    def find_middle(self, head):
        if head is None:
            return head

        small = head
        large = head
        while large.next is not None and large.next.next is not None:
            small = small.next
            large = large.next.next
        return small

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
        self.show_linkedList(self.head)

    def sortedMerge(self, a, b):
        res = None

        if a is None:
            return b
        if b is None:
            return a
        if a.data <= b.data:
            res = a
            res.next = self.sortedMerge(a.next, b)
        else:
            res = b
            res.next = self.sortedMerge(a, b.next)
        return res

    def MergeSort(self, head):
        if head is None or head.next is None:
            return head
        middle = self.find_middle(head)
        nextToMiddle = middle.next
        middle.next = None

        left = self.MergeSort(head)
        right = self.MergeSort(nextToMiddle)

        sortedList = self.sortedMerge(left, right)
        return sortedList

def MergeTwoSortedLinkedList(head1, head2):
    if head1 is None:
        return head2
    if head2 is None:
        return head1
    p, q = head1, head2
    if head1.data < head2.data:
        s = head1
        p = s.next
    else:
        s = head2
        q = s.next
    start = s

    while p is not None or q is not None:
        if p.data < q.data:
            s.next = p
            s = p
            p = p.next
            if p is None:
                s.next = q
                break
        else:
            s.next = q
            s = q
            q = q.next
            if q is None:
                s.next = q
                break

    while start is not None:
        print(f"|{start.data}|->", end=" ")
        start = start.next
    print("NULL")



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
    ll.show_linkedList(ll.head)
    print(ll.find_middle(ll.head).data)
    ll.insert_at_beginning(100)
    ll.show_linkedList(ll.head)
    ll.partial_reverse(2, 11)
    print("=" * 85)

    sortedList1 = LinkedList()
    sortedList1.insert(-20)
    sortedList1.insert(20)
    sortedList1.insert(50)
    sortedList1.insert(70)
    sortedList1.insert(90)
    sortedList1.insert(100)
    sortedList1.insert(1000)

    sortedList2 = LinkedList()
    sortedList2.insert(10)
    sortedList2.insert(30)
    sortedList2.insert(50)
    sortedList2.insert(60)
    sortedList2.insert(80)

    MergeTwoSortedLinkedList(sortedList1.head, sortedList2.head)

    unsortedList = LinkedList()
    unsortedList.insert(20)
    unsortedList.insert(-40)
    unsortedList.insert(60)
    unsortedList.insert(10)
    unsortedList.insert(25)
    unsortedList.insert(0)

    unsortedList.head = unsortedList.MergeSort(unsortedList.head)
    unsortedList.show_linkedList(unsortedList.head)

