#  Сложный вариант - количество кубиков задается условием count
def combinationCount(count, faces):
    if count > 0:
        return recursiveCounter(1, count, faces)
    else:
        return 0

#  Вариант с 4 кубами
def recursiveCounter(depth, maxDepth, faces):
    count = 0
    for i in range(1, faces + 1):
        if depth == maxDepth:
            count += 1
        else:
            count += recursiveCounter(depth + 1, maxDepth, faces)
    return count


count = 3
faces = 6
print("Количество комбинаций: {1} для {0} кубиков"
      .format(count, combinationCount(count, faces)))
