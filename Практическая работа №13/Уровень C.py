import random

array = [random.randint(2, 100) for _ in range(10)]


def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


prime_numbers = [num for num in array if is_prime(num)]
average_prime = sum(prime_numbers) / len(prime_numbers) if prime_numbers else 0
print("Массив: ")
print(' '.join(map(str, array)))
print("Простые числа: ")
print(' '.join(map(str, prime_numbers)))
print(f"Среднее арифметическое простых чисел: {average_prime}")

