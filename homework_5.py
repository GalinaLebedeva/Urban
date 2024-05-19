# 1. Работа со списками

my_list = ['apple', 'peach', 'pineapple', 'watermelon', 'melon']
print(my_list)
print(my_list[-1])
print(my_list[0], my_list[-1])
print(my_list[2:6])
my_list[2] = 'coconut'
print(my_list)

# 2. Работа со словарями

my_dict = {"кот":'cat',"собака":'dog', "корова":'cow', "лошадь":'horse', "бобер":'beaver'}
print(my_dict)
print(my_dict['лошадь'], my_dict.get(('лошадь')))
my_dict['бык'] = 'bull'
my_dict['кот'] = 'dull'
print(my_dict)
