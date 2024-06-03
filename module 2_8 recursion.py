# Задача "Рекурсивное умножение цифр":
# Напиши функцию get_multiplied_digits, которая принимает аргумент целое чиcло number
# и подсчитывает произведение цифр этого числа.


def get_multiplied_digits(number):
    str_number = str(number)
    first = int(str_number[0])
    if len(str_number) <= 1:
        return first
    else:
        res = first * get_multiplied_digits(int(str_number[1:]))
        return res


number = input('Введите Ваше число: ')
result = get_multiplied_digits(number)

print(f'Произведение цифр числа {number}: {result}')
