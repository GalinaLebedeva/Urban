# Задача "За честь и отвагу!"
import time
from threading import Thread
from time import sleep


class Knight(Thread):
    def __init__(self, name: str, power: int):
        super().__init__()
        self.name = name
        self.power = power


    def run(self):
        enemy = 100
        print(f'{self.name}, на нас напали!')
        for i in range(1, enemy + 1):
            enemy -= self.power
            time.sleep(1)
            if enemy == 0:
                print(f'{self.name} одержал победу спустя {i} дней(дня)! Ура!')
                break
            print(f'{self.name} сражается {i} дней (дня), осталось {enemy} воинов.')



first_knight = Knight('Sir Lancelot', 10)
first_knight.start()
time.sleep(1)
second_knight = Knight("Sir Galahad", 20)
second_knight.start()
