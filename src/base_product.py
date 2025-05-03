from abc import ABC, abstractmethod


class BaseProduct(ABC):
    """Абстрактный метод для класса Product"""

    @classmethod
    @abstractmethod  # pragma: no cover
    def new_product(cls, product_dict: dict):  # type: ignore
        pass

    @property
    @abstractmethod  # pragma: no cover
    def price(self):  # type: ignore
        pass

    @price.setter
    @abstractmethod  # pragma: no cover
    def price(self, price: float):  # type: ignore
        pass
