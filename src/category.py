from typing import Any

from src.product import Product


class Category:
    """Класс для представления категории продуктов"""

    category_count = 0
    product_count = 0
    product_count_total = 0

    def __init__(self, name: str, description: str, products: list) -> None:
        self.name = name
        self.description = description
        self.__products = products
        Category.category_count += 1
        Category.product_count += len(products)
        Category.product_count_total = sum([x.quantity for x in self.__products])

    def __str__(self) -> str:
        return f"{self.name}, количество продуктов: {Category.product_count_total} шт."

    def add_product(self, product: Product) -> None:
        if isinstance(product, Product):
            self.__products.append(product)
            Category.product_count += 1
        else:
            raise TypeError

    @property
    def products(self) -> str:
        products_str = ""
        for prod in self.__products:
            products_str += f"{prod}\n"
        return products_str

    def middle_price(self) -> Any:
        try:
            avg_prod_price = sum([x.price for x in self.__products]) / len(self.__products)
        except ZeroDivisionError:
            return 0
        else:
            return round(avg_prod_price, 2)
