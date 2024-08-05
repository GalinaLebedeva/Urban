def add_everything_up(a, b):
    try:
        res = round(a + b, 3)
    except TypeError as exc:
        if (isinstance(a, int) and isinstance(b, str)) or (isinstance(b, int) and isinstance(a, str)):
            return str(a) + str(b)
        if (isinstance(a, float) and isinstance(b, str)) or (isinstance(b, float) and isinstance(a, str)):
            return f'Я не умею складывать разные типы данных - {exc}'
    else:
        return res
    


print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))
