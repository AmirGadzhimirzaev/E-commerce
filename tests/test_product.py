import pytest

from src.product import Product


@pytest.fixture
def test_product():
    return Product("Samsung", "Smartphone with android OS", 50_000, 1)


def test_product_init_fix(test_product):
    assert test_product.name == "Samsung"
    assert test_product.description == "Smartphone with android OS"
    assert test_product.price == 50_000
    assert test_product.quantity == 1


def test_product_init_my(capsys):
    product_1 = Product.new_product({"name": "a", "description": "b", "price": -1000, "quantity": 2})

    assert product_1.name == "a"
    assert product_1.description == "b"
    assert product_1.price == -1000
    assert product_1.quantity == 2

    product_1.price = 0
    message = capsys.readouterr()
    assert message.out.strip() == "Цена не должна быть нулевая или отрицательная"

    product_1.price = 1000
    assert product_1.price == 1000
    assert str(product_1) == "a, 1000 руб. Остаток: 2 шт."
    assert product_1 + product_1 == 4000
