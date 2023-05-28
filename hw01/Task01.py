def heapSort(arr):
    buildMaxHeap(arr)
    size = len(arr) - 1
    for i in range(size, -1, -1):
        # print(arr)
        arr[size], arr[0] = arr[0], arr[size]
        size -= 1
        siftDown(arr, size)
        # print(arr)
    return arr

def buildMaxHeap(arr):
    size = len(arr)
    for i in range(size // 2, -1, -1):
        # print(arr)
        siftDown(arr, size)
        # print(arr)
    return arr


def siftDown(arr, i):
    for k in range(i//2-1, -1, -1):
        # if k == 0:
        #     left = 1
        #     right = 2
        # else:
        left = 2 * k + 1
        right = 2 * k + 2
        print(k, left, right)
        if arr[left] > arr[right]:
            if arr[k] < arr[left]:
                arr[k], arr[left] = arr[left], arr[k]
                print(arr)
            # else:
            #     break
        else:
            if arr[k] < arr[right]:
                arr[k], arr[right] = arr[right], arr[k]
                print(arr)
            # else:
            #     break

        # print(arr)
    return arr


arr = [4, 3, 2, 5, 1, 7, 10, 12, 14, 22, 6]
buildMaxHeap(arr)

# res = heapSort(arr)
# print(res)
# res2 = heapSort(res)
# print(res2)

# print(heapSort(arr))
