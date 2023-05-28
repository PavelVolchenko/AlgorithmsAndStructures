def heapSort(arr):
    buildMaxHeap(arr)
    children = len(arr)
    for i in range(children, 1, -1):
        # Свапаем первый элемент (максимальный по значению) с последним и забываем про него
        # уменьшая размер массива (кол-во потомков для проверки, т.к. он уже отсортирован)
        arr[children - 1], arr[0] = arr[0], arr[children - 1]
        children -= 1
        # Опять проверяем и чиним дерево, т.к. на первом месте может стоять элемент
        # с любым значением и ломать наше дерево
        siftDown(arr, children)
    return arr

# Преобразования исходного массива в бинарное дерево.
def buildMaxHeap(arr):
    [siftDown(arr, len(arr)) for _ in range(len(arr) // 2, 1, -1)]
    return arr

# "Чиним" бинарное дерево (функция "утапливания" узлов).
# Если значение потомка больше родительского, они меняются местами.
# Проверяем все узлы, снизу в верх (к корневому узлу).
def siftDown(arr, children):
    for child in range(children, 1, -1):
        parent = child // 2 - 1
        if arr[child - 1] > arr[parent]:
            arr[child - 1], arr[parent] = arr[parent], arr[child - 1]
    return arr


arr = [4, 3, 2, 5, 1, 4, 5, 5, 7, 10, 12, 12, 14, 22, 6, 9]
print("Исходный массив:", arr)
print("Бинарное дерево:", buildMaxHeap(arr))
print("Отсортированный:", heapSort(arr))
