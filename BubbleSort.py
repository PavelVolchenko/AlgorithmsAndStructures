def BubbleSort(arr):
    while flag:
        for i in range(len(arr) - 1):
            if arr[i] < arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
            else:
                flag = False
        return arr


array = [9, 7, 6, 3, 4, 5, 12, 0]
print(BubbleSort(array))