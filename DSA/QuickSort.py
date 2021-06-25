def QuickSort(arr, left, right):
    if left < right:
        partitionIndex = partition(arr, left, right)
        QuickSort(arr, left, partitionIndex-1)
        QuickSort(arr, partitionIndex+1, right)
        return arr
def partition(arr, left, right):
    pivotElement = arr[right]
    partitionIndex = left
    for j in range(left, right):
        if arr[j] < pivotElement:
            swap(arr, partitionIndex, j)
            partitionIndex += 1
    swap(arr, partitionIndex, right)
    return partitionIndex
def swap(arr, x, y):
    arr[x], arr[y] = arr[y], arr[x]

print(QuickSort([23, 6, 4, -1, 0, 12, 8, 3, 1], 0, 8))


def HoareQuickSelect(arr, left, right, indexToFind):
    if left < right:
        partitionIndex = partition(arr, left, right)
        if indexToFind < partitionIndex:
            HoareQuickSelect(arr, left, partitionIndex-1, indexToFind)
        elif indexToFind > partitionIndex:
            HoareQuickSelect(arr, partitionIndex+1, right, indexToFind)
        else:
            return arr[partitionIndex]
def getKthLargest(arr, k):
    idx = len(arr) - k
    HoareQuickSelect(arr, 0, len(arr)-1, idx)
    return arr[idx]


print(getKthLargest([2, 4, 1, 9, -5, 6, 3], 1))
