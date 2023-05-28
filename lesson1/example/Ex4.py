#  Фибоначчи через рекурсию
#  (экспоненциальная сложность)
def fb(n):
    if n <= 2:
        return 1
    else:
        return fb(n - 1) + fb(n - 2)


n = 10
print("Фибоначчи {} = {}".format(n, fb(n)))
