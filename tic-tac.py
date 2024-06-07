# Проверка победителя

def check_winner():
    if area[0][0] == 'O' and area[0][1] == 'O' and area[0][2] == 'O':
        return '0'
    if area[1][0] == 'O' and area[1][1] == 'O' and area[1][2] == 'O':
        return '0'
    if area[2][0] == 'O' and area[2][1] == 'O' and area[2][2] == 'O':
        return '0'
    if area[0][0] == 'O' and area[1][0] == 'O' and area[2][0] == 'O':
        return '0'
    if area[0][1] == 'O' and area[1][1] == 'O' and area[2][1] == 'O':
        return '0'
    if area[0][2] == 'O' and area[1][2] == 'O' and area[2][2] == 'O':
        return '0'
    if area[0][0] == 'O' and area[1][1] == 'O' and area[2][2] == 'O':
        return '0'
    if area[0][2] == 'O' and area[1][1] == 'O' and area[2][0] == 'O':
        return '0'
    if area[0][0] == 'X' and area[0][1] == 'X' and area[0][2] == 'X':
        return 'X'
    if area[1][0] == 'X' and area[1][1] == 'X' and area[1][2] == 'X':
        return 'X'
    if area[2][0] == 'X' and area[2][1] == 'X' and area[2][2] == 'X':
        return 'X'
    if area[0][0] == 'X' and area[1][0] == 'X' and area[2][0] == 'X':
        return 'X'
    if area[0][1] == 'X' and area[1][1] == 'X' and area[2][1] == 'X':
        return 'X'
    if area[0][2] == 'X' and area[1][2] == 'X' and area[2][2] == 'X':
        return 'X'
    if area[0][0] == 'X' and area[1][1] == 'X' and area[2][2] == 'X':
        return 'X'
    if area[0][2] == 'X' and area[1][1] == 'X' and area[2][0] == 'X':
        return 'X'
    return '*'

# Создаем наше поле для игры

rows = 3
columns = 3

area = []
for i in range(1,rows + 1):
    new = []
    for j in range(1, columns + 1):
        new.append('*')
    area.append(new)

# Создаем функцию для наглядного вывода поля

def draw_area():
    for k in area:
        print(*k)

draw_area()

#Создаем игру с переходом хода, сначала ходят крестики, потом нолики

for turn in range(1,10):
    print(f'Ход: {turn}')
    if turn % 2 == 0:
        turn_char = 'O'
        print('Ходят нолики')
    else:
        turn_char = 'X'
        print('Ходят крестики')
    a = int(input('Введите строку для хода 1,2 или 3: ')) - 1
    b = int(input('Введите столбец для хода 1,2 или 3: ')) - 1
    if area[a][b] == '*':
        area[a][b] = turn_char
    else:
        print('Ячейка уже занята, Вы пропускаете ход')
        draw_area()
        continue
    draw_area()

    if check_winner() == 'X':
        print('Выиграли крестики')
        break
    elif check_winner() == '0':
        print('Выиграли нолики')
        break
    elif check_winner() == '*' and turn == 9:
        print('Ничья')
        break

