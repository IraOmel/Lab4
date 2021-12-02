class Product:
    def __init__(self, name, quantity, price):
        self.name = name
        self.quantity = quantity
        self.price = price

    @property
    def price(self):
        return self._price

    @property
    def quantity(self):
        return self._quantity

    @price.setter
    def price(self, price):
        if not isinstance(price, float):
            raise TypeError("incorrect type")
        if price < 0 or not price:
            raise ValueError("incorrect value")
        self._price = price

    @quantity.setter
    def quantity(self, quantity):
        if not isinstance(quantity, int):
            raise TypeError("incorrect type")
        if quantity < 0 or not quantity:
            raise ValueError("incorrect value")
        self._quantity = quantity

    def __setattr__(self, name, value):
        super(Product, self).__setattr__(name, value)

    def __repr__(self):
        # res = ', '.join(map(str, self.__dict__.values()))
        return f'\n{self.__dict__}\n'


class Composition:
    """A class that contain data about products."""

    def __init__(self, products):
        self.products = products

    @property
    def products(self):
        return self._products

    @products.setter
    def products(self, products):
        if not all([isinstance(product, Product) for product in products]):
            raise TypeError("incorrect type")
        self._products = products

    def add_product(self, product):
        if not isinstance(product, Product):
            raise TypeError
        self.products.append(product)

    def del_product(self, product):
        if not isinstance(product, Product):
            raise TypeError
        if product not in self.products:
            raise ValueError("no such product")
        self.products.remove(product)

    def __contains__(self, find_product):
        for item in self.products:
            if item.name == find_product:
                return f'\nProduct found: {item}'
        return f'{find_product} - no such product'

    def __str__(self):
        return f'Composition: {self.products}'


obj1 = Product("Tangerine", 5, 2.5)
obj1.country = 'Spain'
obj2 = Product("Apple", 5, 2.5)
obj2.description = "Red"
obj3 = Product("Orange", 10, 2.5)
composition = Composition([obj1, obj2])
composition.add_product(obj3)
print(composition)
# print("Apple" in composition)
print(composition.__contains__("Apple"))
print(composition.__contains__("Lemon"))

