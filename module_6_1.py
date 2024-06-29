# Задача "Съедобное, несъедобное":
# Разнообразие животного мира давно будоражит умы человечества. Царства, классы, виды...
# Почему бы и нам не попробовать выстроить что-то подобное используя наследования классов?
#
# Необходимо описать пример иерархии животного мира, используя классы и принцип наследования.

class Animal():
    """ Класс животное с тремя атрибутами: alive (живой), fed (накормленный), name """

    alive = True
    fed = False
    food = None

    def __init__(self, name):
        self.name = name

class Plant():
    """ Класс растение с двумя атрибутами: edible (съедобность), name"""
    edible = False

    def __init__(self, name):
        self.name = name


class Flower(Plant):
    """ Класс цветок, дочерний от класса растение"""

class Fruit(Plant):
    """ Класс фрукт с переопределенным оператором edible, дочерний от класса растение"""
    edible = True

class Mammal(Animal, Plant):
    """ Класс млекопитающее с атрибутом food и методом eat (food), дочерний от класса животные и класса Растение"""

    def __init__(self, name):
        super().__init__(name)
        self.food = Fruit.edible

    def eat(self, food):
        if self.food == False:
            print(f'{self.name} не стал есть {food.name}')
            self.alive = False
        elif self.food == True:
            print(f'{self.name} cъел {food.name}')
            self.fed = True

class Predator(Animal, Plant):
    """ Класс хищник с атрибутом food и методом eat (food), дочерний от класса животные и класса Растение"""

    def __init__(self, name):
        super().__init__(name)
        self.food = Flower.edible

    def eat(self, food):
        if self.food == False:
            print(f'{self.name} не стал есть {food.name}')
            self.alive = False
        elif self.food == True:
            print(f'{self.name} cъел {food.name}')
            self.fed = True


a1 = Predator('Гепард')
a2 = Mammal('Пёс Барбос')
p1 = Flower('Герань')
p2 = Fruit('Банан')

print(a1.name)
print(p1.name)

print(a1.alive)
print(a2.fed)
a1.eat(p1)
a2.eat(p2)
print(a1.alive)
print(a2.fed)
