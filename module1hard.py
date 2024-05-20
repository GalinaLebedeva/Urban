#Задание:
# Напишите программу, которая составляет словарь, используя grades и students, где ключом будет имя ученика, а значением - его средний балл.

#Переменная students - это множество, поэтому перед решением, нужно перевести её в список и отсортировать по алфавиту,
#так как, согласно заданию список grades содержит списки оценок для каждого ученика в алфавитном порядке.

grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

#Вариант ручного перебора каждого элемента

dct = {}
# print(type(grades))
# print(type(students))
students = list(students)
# print(type(students))
students.sort()

ST1 = students[0]
Mark1 = sum(grades[0])/len(grades[0])

ST2 = students[1]
Mark2 = sum(grades[1])/len(grades[1])

ST3 = students[2]
Mark3 = sum(grades[2])/len(grades[2])

ST4 = students[3]
Mark4 = sum(grades[3])/len(grades[3])

ST5 = students[4]
Mark5 = sum(grades[4])/len(grades[4])

dct.update(dict([[ST1,Mark1]]))
dct.update(dict([[ST2,Mark2]]))
dct.update(dict([[ST3,Mark3]]))
dct.update(dict([[ST4,Mark4]]))
dct.update(dict([[ST5,Mark5]]))
print(dct)

# Вариант с помощью функции zip для переборки значений в переменной students и grades.
#Так как в переменной grades список всех оценок, среднюю оценку записываем в переменную marks.

marks = [Mark1,Mark2,Mark3,Mark4,Mark5]
st = dict(zip(students, marks))
print(st)