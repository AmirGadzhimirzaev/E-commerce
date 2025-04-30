import pytest

from src.product import Product


@pytest.fixture
def product():
    return Product("Samsung", "Smartphone with android OS", 50_000, 1)


def test_product_init(product):
    assert product.name == "Samsung"
    assert product.description == "Smartphone with android OS"
    assert product.price == 50_000
    assert product.quantity == 1
