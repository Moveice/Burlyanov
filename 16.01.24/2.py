a, b, c = [int(i) for i in input('Введите три числа: ').split()]
if a == b  == c:
    print('Все числа одинаковые.')
elif a == b or a == c:
    print('Два числа одинаковые.')
elif b == a or b == c:
    print('Два числа одинаковые.')
elif c == a or c == b:
    print('Два числа одинаковые.')
else:
    print('Нет одинаковых чисел.')