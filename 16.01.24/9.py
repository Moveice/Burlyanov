a = int(input('Введите трехзначное число: '))
hund = (a // 100) % 10
tens = (a // 10) % 10
units = a % 10
sum1 = hund + tens
sum2 = tens + units
if sum1 > sum2:
    print(sum1, sum2, sep='')
else:
    print(sum2, sum1, sep='')

