# Что должно быть подсчитано:
#
# 1. Все числа (не важно, являются они ключами или значениям или ещё чем-то).
# 2. Все строки (не важно, являются они ключами или значениям или ещё чем-то)


data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]


def calculate_data_structure(data_structure):

    sum = 0

    if isinstance(data_structure, (int,float)):  # Основные типы данных - int, float, str, bool
        sum += data_structure                    # Поэтому их мы складываем в первую очередь
    elif isinstance(data_structure, str):        # Далее раскладываем элементы по структурам данных
        sum += len(data_structure)               # Если данные в списке, кортеже или множестве, распаковываем эту структуру и далее функция считает количество символов
    elif isinstance(data_structure, bool):       # Также делаем со словарем, отдельно считаем по ключам и по значениям словаря
        sum += data_structure                    #
    elif isinstance(data_structure, (list, tuple, set)):
        for item in data_structure:
            sum += calculate_data_structure(item)
    elif isinstance(data_structure, dict):
        for keys,value in data_structure.items():
            sum += calculate_data_structure(keys)
            sum += calculate_data_structure(value)
    return sum


result = calculate_data_structure(data_structure)
print(result)