a = int(input('Введите номер месяца: '))
if a > 12 or a == 0:
    print('Неверный номер месяца.')
elif a <= 3:
    print('Зима')
elif a <= 6 and a > 3:
    print('Весна')
elif a <= 9 and a > 6:
    print('Лето')
else:
    print('Осень')