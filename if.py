#Самостоятельная работа по уроку "Цели и задачи. Поток выполнения программы. Как интерпретатор показывает переменные."

# 1 Task
x = 27
print('Hello')
if x  < 0:
    print('Less zero')
print('Good bye')

# 2 Task

a, b = 5, 10
if a > b:
    print('a > b')
if a > b and a > 0:
    print('Success')
if (a > b) and (a > b or b < 1000):
    print('Success')
if 5 < b  and b < 10:
    print('Success')

# 3 Task

if '23' > '43':
    print('Success')
if '123' > '12':
    print('Success')
if [1,2] > [1,1]:
    print('Success')

# $ Task. We can't compare different type of data.

# if '6' > 5:
#     print('Success')
# if [5,6]> 5:
#     print('Success')
 # but

if '6' != 5:
    print('Success')