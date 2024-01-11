import random
results = []
for _ in range(3):
    result = random.randint(1,6)
    results.append(result)
aver = sum(results)/len(results)
print('Выпало очков')
print(*results, sep='')
print('Среднее значение: ',aver)
