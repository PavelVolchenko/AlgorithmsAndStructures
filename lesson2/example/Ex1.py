import random

# Пузырьковая сортировка. Сложность O(n^2)
def bubbleSort(arr):
    flag = True
    while flag:
        flag = False
        for i in range(len(arr) - 1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                flag = True
    return arr

# Сортировка выбором. Сложность O(n^2)
def directSort(arr):
    for i in range(len(arr) - 1):
        minPos = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[minPos]:
                minPos = j
        if minPos != i:
            arr[minPos], arr[i] = arr[i], arr[minPos]
    return arr

# Сортировка вставками. Сложность O(n^2)
def insertSort(arr):
    for i in range(len(arr) - 1):
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[i]:
                arr[j], arr[i] = arr[i], arr[j]
    return arr


# # # # # # # # # # # # # # # # # # # # # # # # # # #
#  Вариант с подсчетом итераций и выводом в консоль #
# # # # # # # # # # # # # # # # # # # # # # # # # # #
def bubbleSortConsole(arr):
    count = 1
    flag = True
    while flag:
        flag = False
        for i in range(len(arr) - 1):
            count += 1
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                flag = True
    print("Пузырьковая сортировка.", end=' ')
    print("{} итераций".format(count))
    return arr

def directSortConsole(arr):
    count = 1
    for i in range(len(arr) - 1):
        minPos = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[minPos]:
                minPos = j
                count += 1
        if minPos != i:
            arr[minPos], arr[i] = arr[i], arr[minPos]
            count += 1
        count += 1
    print("    Сортировка выбором.", end=' ')
    print("{} итераций".format(count))
    return arr

def insertSortConsole(arr):
    count = 1
    for i in range(len(arr) - 1):
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[i]:
                arr[j], arr[i] = arr[i], arr[j]
                count += 1
            count += 1
        count += 1
    print("  Сортировка вставками.", end=' ')
    print("{} итераций".format(count))
    return arr


size = 100  # Размерность массива
randArr = list()
[randArr.append(random.randint(0, 100)) for _ in range(size)]
print(f"Для массива из {len(randArr)} эл.:", *randArr[:8], "...")
bubbleSortConsole(randArr)
directSortConsole(randArr)
insertSortConsole(randArr)