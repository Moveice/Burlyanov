import random
A, B = map(int, input('Введите границы диапазона:\n ').split())
array = []
for _ in range(5):
    array.append(random.randint(A, B))
print('Массив\n', array)
