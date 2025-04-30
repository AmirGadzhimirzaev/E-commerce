from src.product import Product


class Category:
    """Класс для представления категории продуктов"""

    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products: list) -> None:
        self.name = name
        self.description = description
        self.__products = products
        Category.category_count += 1
        Category.product_count = len(self.__products)

    def add_product(self, product: Product) -> None:
        self.__products.append(product)
        Category.product_count += 1

    @property
    def products(self) -> str:
        products_str = ""
        for prod in self.__products:
            products_str += f"{prod.name}, {prod.price} руб. Остаток: {prod.quantity} шт.\n"
        return products_str
