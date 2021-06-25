def MergeSort(arr):
    # Divide Phase

    # base case: keep splitting until we get single element array.
    length = len(arr)
    if length == 1:
        return
    mid = length//2
    left = arr[:mid]
    right = arr[mid:]
    MergeSort(left)
    MergeSort(right)

    # Conquer Phase
    i, j, k = 0, 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            arr[k] = left[i]
            k += 1
            i += 1
        else:
            arr[k] = right[j]
            k += 1
            j += 1
    while i < len(left):
        arr[k] = left[i]
        k += 1
        i += 1
    while j < len(right):
        arr[k] = right[j]
        k += 1
        j += 1

    return arr

print(MergeSort([9, 9, 0, -5, 12, 5, 10]))
