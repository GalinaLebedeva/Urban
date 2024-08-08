first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

first_result = (len(x) - len(y) for x, y in zip(first, second) if len(x) != len(y))
print(list(first_result))

second_result = (len(x[1]) == len(y[1]) for x in enumerate(first) for y in enumerate(second) if x[0] == y[0])
print(list(second_result))

second_result = (len(first[word]) == len(second[word]) for word in range(len(first)))
print(list(second_result))