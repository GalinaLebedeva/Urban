class Vehicle():

    __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']

    def __init__(self, owner:str, __model:str, __engine_power:int, __color:str):
        self.owner = owner
        self.__model = __model
        self.__engine_power = __engine_power
        self.__color = __color

    def get_model(self):
        print(f'Модель: : {self.__model}')

    def get_horsepower(self):
        print(f'Мощность двигателя: {self.__engine_power}')

    def get_color(self):
        print(f'Цвет: {self.__color}')

    def print_info(self):
        self.get_model()
        self.get_horsepower()
        self.get_color()
        print(f'Владелец: {self.owner}')

    def set_color(self, new_color:str):
        self.new_color = new_color.lower()
        if self.new_color in self.__COLOR_VARIANTS:
            self.__color = self.new_color
        else:
            print(f"Нельзя сменить цвет на {self.new_color}")


class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5

# Цветовая палитра
__COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']

# Объект класса Vehicle
vehicle1 = Sedan('Fedos', 'Toyota Mark II', 500, 'blue')


# Изначальные свойства
vehicle1.print_info()

# Меняем свойства (в т.ч. вызывая методы)
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'

# Проверяем что поменялось
vehicle1.print_info()