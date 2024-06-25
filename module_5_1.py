#1.  Задача "Developer - не только разработчик"

class House():
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        if new_floor > self.number_of_floors or new_floor < 1:
            print('Такого этажа не существует')
        else:
            for i in range(1, new_floor + 1):
                print(i)



h1 = House('ЖК Камчатка', 18)
h2 = House('Дом в Луйсковицах', 2)
h1.go_to(7)
h2.go_to(3)

h1 = House('ЖК Камчатка', 18)
print(h1.name, h1.number_of_floors)
h2 = House('Дом в Луйсковицах', 2)
h1.go_to(5)
h2.go_to(3)

#2. Задача с переопределением атрибута Количество этажей

class House2 ():

    def __init__(self):
        self.numberOfFloors = 0

    def setNewNumberOfFloors (self, floors):
        self.setNewNumberOfFloors = floors
        self.numberOfFloors = self.setNewNumberOfFloors

h1 = House2()
print(h1.numberOfFloors)
h1.setNewNumberOfFloors(2)
print(h1.numberOfFloors)

# 3. Задача с перегрузкой оператора equal

class Building():
    def __init__(self, numberOfFloors, buildingType):
        self.numberOfFloors = int(numberOfFloors)
        self.buildingType = str(buildingType)

    def __eq__(self, other):
        return self.numberOfFloors == other.numberOfFloors and self.buildingType == other.buildingType

    def __str__(self):
        return f'Число этажей: {self.numberOfFloors}, Тип здания: {self.buildingType}'

B1 = Building(2, 'private house')
B2 = Building(2, 'private house')
print(B1)
print(B2)
print(B1 == B2)
B1.numberOfFloors = 3
print(B1)
print(B2)
print(B1 == B2)

#4. Задача по созданию экземпляров объекта

class Building2():
    total = 0

    def __init__(self):
        Building2.total += 1


for i in range(Building2.total, 40):
    if Building2.total == 40:
        break
    build = Building2()
    print(build)

print(Building2.total)
