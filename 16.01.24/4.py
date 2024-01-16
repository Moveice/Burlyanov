a = int(input('Введите возраст: '))
if a > 120:
    print('Введен слишком большой возраст')
elif a == 1 or a % 10 == 1 and a != 11:
    print(f"Вам {a} год")
elif a == 2 or a % 10 == 2 and a != 12 and a < 120:
    print(f"Вам {a} года")
elif a == 3 or a % 10 == 3 and a != 13 and a < 120:
    print(f"Вам {a} года")
elif a == 4 or a % 10 == 4 and a != 14 and a < 120:
    print(f"Вам {a} года")
else:
    print(f"Вам {a} лет")