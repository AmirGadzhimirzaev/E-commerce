import pytest
from unicodedata import category

from src.templates import Product, Category


@pytest.fixture
def product():
    return Product('Samsung', 'Smartphone with android OS', 50_000, 1)


@pytest.fixture
def group_of_products():
    return Category('Smartphones', 'Best smartphones in country',
                    [Product('Samsung', 'smartphone', 40_000, 1)])


def test_product_init(product):
    assert product.name == 'Samsung'
    assert product.description == 'Smartphone with android OS'
    assert product.price == 50_000
    assert product.quantity == 1


def test_category_init(group_of_products):
    assert group_of_products.name == 'Smartphones'
    assert group_of_products.description == 'Best smartphones in country'
    assert group_of_products.products == ['Samsung']
    assert group_of_products.category_count == 1
    assert len(group_of_products.products) == 1
