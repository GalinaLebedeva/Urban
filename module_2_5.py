# Цель: закрепить навык написания функций и их вызовов.

# Задача "Матрица воплоти":
# Напиши функцию get_matrix с тремя параметрами n, m и value, которая будет создавать матрицу(вложеный список)
# размерами n строк и m столбцов, заполненную значениями value и возвращать эту матрицу в качестве результата работы.

def get_matrix(n, m, value):
    matrix = []
    for i in range(n):
        first = []
        for j in range(m):
            first.append(value)
        matrix.append(first)
    print(matrix)


n = 3
m = 2
value = 10
get_matrix(n, m, value)