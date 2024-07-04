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

    def eat(self, food):
        if not food.edible:
            print(f'{self.name} не стал есть {food.name}')
            self.alive = False
        else:
            print(f'{self.name} cъел {food.name}')
            self.fed = True


class Plant():
    """ Класс растение с двумя атрибутами: edible (съедобность), name"""

    edible = False

    def __init__(self, name):
        self.name = name


class Flower(Plant):
    """ Класс цветок, дочерний от класса растение"""
    pass


class Fruit(Plant):
    """ Класс фрукт с переопределенным оператором edible, дочерний от класса растение"""
    edible = True


class Mammal(Animal):
    pass


class Predator(Animal):
    pass


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
