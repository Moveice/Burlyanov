number = int(input('Введите натуральное число: '))
rim_numbers = {
    1000: 'M',
    900: 'CM',
    500: 'D',
    400: 'CD',
    100: 'C',
    90: 'XC',
    50: 'L',
    40: 'XL',
    10: 'X',
    9: 'IX',
    5: 'V',
    4: 'IV',
    1: 'I',
}
rim_number = ''
for value, symbol in rim_numbers.items():
    while number >= value:
        rim_number += symbol
        number -= value
print(rim_number)
