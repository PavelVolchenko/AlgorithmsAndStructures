def binSort(arr, start, end, value):
    if end < start:
        return -1
    pivot = (start + end) // 2
    if arr[pivot] > value:
        return binSort(arr, start, pivot - 1, value)
    elif arr[pivot] < value:
        return binSort(arr, pivot + 1, end, value)
    else:
        return pivot


arr = [9, 7, 6, 3, 4, 5, 12, 0, 45, 23]
sortArr = sorted(arr)
print(sortArr)
print(binSort(sortArr, 0, len(sortArr), 5))
