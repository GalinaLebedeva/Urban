# Задание 1. Программа, выдающая длину строки

my_string = input("Введите текст ")

if my_string != ' ':
    print(len(my_string))
else:
    count = 1
    while my_string == ' ' or count!= 2:
        str = input("Попробуй снова ")
        count +=1
        if  str!= ' ':
            print(len(str))
            break
        if count == 2:
            print('Введи наконец текст')
            stri = input('Текст: ')
            print(len(stri))
            break

# Задание 2. Методы строк

full_name = input("Введите ФИО: ")
print(full_name.upper())
print(full_name.lower())
print(full_name.replace(' ',''))
print(full_name[0])
print(full_name[-1])

