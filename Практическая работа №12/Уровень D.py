import random
n = int(input('ведите n: '))
array = [i for i in range(1, n + 1)]
for i in range(n):
    j = random.randint(0, i)
    array[i], array[j] = array[j], array[i]
print('Массив:')
print(' '.join(map(str, array)))