immutable_var = (1, 'cat', True, 5.5)
print(immutable_var)


# Попытка изменить кортеж
# immutable_var[0] = 3


# Кортеж - неизменяемый тип объекта, поэтому изменить первый элемент в нем невозможно, о чем говорит нам консоль.
# Но, если создать кортеж из списка и других типов данных, то все получится)

immutable_var = (1, 'dog', [3,'apple', 2], True)
print(immutable_var)
immutable_var[2][1] = 'pomidoro'
print(immutable_var)

mutable_list = [1,2,3,5,6,7]
mutable_list.append(6)
print(mutable_list)
mutable_list.pop(2)
print(mutable_list)
mutable_list.extend([1,3])
print(mutable_list)
mutable_list.insert(3, 'cat')
print(mutable_list)
mutable_list.remove(3)
print(mutable_list)
