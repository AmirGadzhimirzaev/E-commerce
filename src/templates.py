class Product:
    """Класс для представления продукта"""

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity


class Category:
    """Класс для представления категории продуктов"""

    category_count = 0
    product_count = 0

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.products = [x.name for x in products]
        Category.category_count += 1
        Category.product_count += 1
