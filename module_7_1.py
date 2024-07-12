import pprint as pp

class Product():
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'

class Shop():
    def __init__(self):
        self.__filename = 'products.txt'

    def get_products(self):
        file = open(self.__filename, 'r')
        products_list = file.read()
        file.close()
        return products_list

    def add(self, *products):
        exist_products = self.get_products()
        file = open(self.__filename, 'a')
        for product in products:
            if product.name not in exist_products:
                file.write(product.__str__() + '\n')
                exist_products += product.name
            else:
                print(f'Продукт {product.name} уже есть в магазине')


s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2) # __str__

s1.add(p1, p2, p3)

print(s1.get_products())