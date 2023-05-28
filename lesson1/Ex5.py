#  Фибоначи без рекурсии
#  (линейная сложность)
def fb(n):
    if n <= 2:
        return 1
    else:
        result = list()
        result.append(1)
        result.append(1)
        for i in range(2, n):
            result.append(result[i - 1] + result[i - 2])
    return result


n = 10
print("Фибоначчи {} = {}".format(n, fb(n)))
