import random
import threading
import time

class Bank():

    lock = threading.Lock()

    def __init__(self):
        self.balance = 0

    def deposit(self):
        for i in range(100):
            check = random.randint(50, 500)
            with Bank.lock:
                self.balance += check
                print(f'Пополнение: {check}. Баланс: {self.balance}')
            time.sleep(0.001)


    def take(self):
        for i in range(100):
            check = random.randint(50, 500)
            with Bank.lock:
                print(f'Запрос на {check}')
                if check <= self.balance:
                    self.balance -= check
                    print(f'Снятие: {check}. Баланс: {self.balance}')
                elif check > self.balance:
                    print('Запрос отклонён, недостаточно средств')
            time.sleep(0.001)


bk = Bank()
th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))
th1.start()
th2.start()
th1.join()
th2.join()
print(f'Итоговый баланс: {bk.balance}')