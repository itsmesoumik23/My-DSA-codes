def binarySearch(arr, left, right, value):
    if left > right:
        return -1
    middle = (left+right)//2
    if arr[middle] < value:
        return binarySearch(arr, middle+1, right, value)
    elif arr[middle] > value:
        return binarySearch(arr, left, middle-1, value)
    else:
        return middle

print(binarySearch([1, 2, 5, 6, 7, 9, 10, 10, 10, 12, 15, 16, 18, 20, 24, 25, 56, 60, 75], 0, 18, 25))

def RangeTarget(arr, left, right, target):
    firstPosition = binarySearch(arr, left, right, target)
    start, end = firstPosition, firstPosition
    if firstPosition == -1:
        return [-1, -1]
    while start != -1:
        temp = start
        start = binarySearch(arr, left, start-1, target)
    start = temp
    while end != -1:
        temp = end
        end = binarySearch(arr, end+1, right, target)
    end = temp
    return [start, end]

print(RangeTarget([1, 2, 5, 6, 7, 9, 10, 10, 10, 12, 15, 16, 18, 20, 24, 25, 56, 60, 75], 0, 18, 10))
