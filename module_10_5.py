import datetime
import os
from multiprocessing import Pool

def read_info(name):
    all_data =[]
    with open(name, 'r', encoding='utf-8') as file:
        for line in file:
            file.readline()
            all_data.append(line)
        print(all_data)

file_names = [f'./file {number}.txt' for number in range(1, 5)]

# Линейный запуск

# start = datetime.datetime.now()
# for file in file_names:
#     read_info(file)
# end = datetime.datetime.now()
# dif = end - start
# print(f'Время работы линейного выполнения программы - {dif} секунд')

# Многопроцессный запуск

if __name__ == '__main__':
    start = datetime.datetime.now()
    with Pool(4) as p:
        res = p.map(read_info, file_names)
    end = datetime.datetime.now()
    dif = end - start
    print(f'Время работы многопроцессного выполнения программы - {dif} секунд')
