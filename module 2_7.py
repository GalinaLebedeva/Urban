def print_params(a=1, b='строка', c=True):
    print(a, b, c)


print_params()
print_params(b=25)
print_params(c=[1, 2, 3])

values_list = [1, 'cat', True]
values_dict = {'a': 'dog', 'b': 34, 'c': [4,5]}
print_params(*values_list)
print_params(**values_dict)

values_list_2 = [[6,7],'scrooge']
print_params(*values_list_2, 42)