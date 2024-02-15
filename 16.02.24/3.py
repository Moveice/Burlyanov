def is_perfect(number):
    dom_of = 0
    for i in range(1,number):
        if number % i == 0:
            dom_of += i
    if dom_of == number:
        return f'Число{number} совершенное'
    else:
        return f'Число{number} не совершенное'
