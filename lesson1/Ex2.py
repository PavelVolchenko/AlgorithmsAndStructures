#  Алгоритм поиска простых чисел в диапазоне от 1 до N.
#  (квадратичная сложность)
def findSimpleNumbers(num):
    result = list()
    count = 0
    for i in range(1, num + 1):
        simple = True
        for j in range(2, i):
            count += 1
            if i % j == 0:
                simple = False
                break
        if simple:
            result.append(i)
    return result, count


n = 35
print("Простые числа от 1 до {0}; "
      "Кол-во итераций: {2}"
      "\n{1}"
      .format(n, *findSimpleNumbers(n)))
