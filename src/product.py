class Product:
    """Класс для представления продукта"""

    def __init__(self, name: str, description: str, price: float, quantity: int) -> None:
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    def __str__(self) -> str:
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other: 'Product') -> float:
        return self.price * self.quantity + other.price * other.quantity

    @classmethod
    def new_product(cls, product_dict: dict) -> 'Product':
        return cls(product_dict["name"], product_dict["description"], product_dict["price"], product_dict["quantity"])

    @property
    def price(self) -> float:
        return self.__price

    @price.setter
    def price(self, price: float) -> None:
        if price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
            return
        self.__price = price
