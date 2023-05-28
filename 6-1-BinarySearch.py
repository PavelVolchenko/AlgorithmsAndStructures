arrA = list(map(int, input().split()))
arrB = list(map(int, input().split()))

for i in range(1, arrA[0] +1):
    for j in range(1, arrA[0] +1):
        if arrB[i] == arrA[j]:
            print(j, end=' ')
            break
        elif j == arrA[0]:
            print('-1', end=' ')
