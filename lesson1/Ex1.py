# Алгоритм, считающий сумму всех чисел от 1 до N.(линейная сложность)
def sumOne(num):
    count = 0
    total = 0
    for i in range(1, num + 1):
        total += i
        count += 1
    return total, count

# Решение с помощью формулы с константной (константная сложность)
def sumTwo(num):
    return ((1 + num) * num) // 2


n = 2200
print("Сумма от 1 до {0} равна {1}: количество итераций {2}".format(n, *sumOne(n)))
print(f"Сумма от 1 до {n} равна {sumTwo(n)}")
