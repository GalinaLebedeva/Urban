import time
from _datetime import datetime as d
from threading import Thread

def wite_words(word_count, file_name):
        with open(file_name, 'w+', encoding='utf-8') as file:
            for i in range(1, word_count + 1):
                file.write(f'Какое-то слово № {i} \n')
                time.sleep(0.1)
            print(f'Завершилась запись в файл {file_name}')

'Стартовая точка отсчёта времени перед выполнением функций. Задержка между записями в файл = 0,1 секунды'

start1 = d.now()
wite_words(10, 'example1.txt')
wite_words(30, 'example2.txt')
wite_words(200, 'example3.txt')
wite_words(100, 'example4.txt')
end1 = d.now()

'Конечная точка отсчёта времени после выполнения функций'
'Печатаем разницу'
time_res = end1 - start1
print(time_res)

'Стартовая точка отсчёта времени перед запуском потоков'
start2 = d.now()

'Аргументы для создания потоков'

a = 10, 'example5.txt'
b = 30, 'example6.txt'
c = 200, 'example7.txt'
e = 100, 'example8.txt'

'Создание потоков (функция, аргументы)'
first = Thread(target=wite_words, args=a)
second = Thread(target=wite_words, args=b)
third = Thread(target=wite_words, args=c)
forth = Thread(target=wite_words, args=e)

'Запуск потоков'

first.start()
second.start()
third.start()
forth.start()

'Ожидание ответов'

first.join()
second.join()
third.join()
forth.join()

'Конечная точка отсчёта времени после выполнения функций'
'Печатаем разницу'

end2 = d.now()
time_res2 = end2 - start2
print(time_res2)
