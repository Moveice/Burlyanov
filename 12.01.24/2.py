import random
results = []
for i in range(3):
    result = random.randint(1,6)
    results.append(str(result))
number = int(''.join(results))
sq = number ** 2
print('Выпало очков')
print(*results, sep='')
print('Число:', number)
print('Его квадрат: ', sq)
