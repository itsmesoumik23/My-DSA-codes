from random import randint

capacity = 50

class MAXHeaps(object):

    def __init__(self):
        self.heap_size = 0
        self.heap = []

    def insert(self, data):
        if self.heap_size == capacity:
            return
        self.heap.append(data)
        self.heap_size += 1

        self.fix_up(self.heap_size-1)

    def fix_up(self, index):
        parent = (index-1) // 2

        if index > 0 and self.heap[index] > self.heap[parent]:
            self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
            self.fix_up(parent)

    def getMax(self):
        return self.heap[0]

    def poll(self):
        maxItem = self.getMax()

        # swap with the last item.
        self.heap[0], self.heap[self.heap_size-1] = self.heap[self.heap_size-1], self.heap[0]
        self.heap_size -= 1

        self.fix_down(0)    #heapify.
        return self.heap

    def fix_down(self, index):

        left, right = 2 * index + 1, 2 * index + 2
        largest = index

        if left < self.heap_size and self.heap[largest] < self.heap[left]:
            largest = left
        if right < self.heap_size and self.heap[largest] < self.heap[right]:
            largest = right

        if index != largest:
            self.heap[largest], self.heap[index] = self.heap[index], self.heap[largest]
            self.fix_down(largest)

    def HeapSort(self):
        for _ in range(self.heap_size):
            self.poll()
        return self.heap

    def convertToMinHeap(self):
        for i in range((len(self.heap)-2)//2, -1, -1):
            self.fix_down(i)
        return self.heap

if __name__ == "__main__":
    heaps = MAXHeaps()
    for _ in range(10):
        heaps.insert(randint(-100, 100))
    print(heaps.heap)

    # print(heaps.HeapSort())
