from random import *
result = randint(100, 999)
hund = (result // 100) % 10
tens = (result // 10) % 10
uni = result % 10
print('Выпало число', result)
print('Сотни: ', hund)
print('Десятки: ', tens)
print('Единицы: ', uni)
