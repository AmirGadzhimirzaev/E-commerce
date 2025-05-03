from abc import ABC, abstractmethod


class BaseProduct(ABC):
    """Абстрактный метод для класса Product"""

    @classmethod
    @abstractmethod  # pragma: no cover
    def new_product(cls, product_dict: dict):
        pass

    @property
    @abstractmethod  # pragma: no cover
    def price(self):
        pass

    @price.setter
    @abstractmethod  # pragma: no cover
    def price(self, price: float):
        pass
