import pytest

from src.category import Category
from src.product import Product

test_product = Product("Samsung", "smartphone", 40_000, 1)

@pytest.fixture
def group_of_products():
    return Category("Smartphones", "Best smartphones in country", [test_product])


def test_category_init(group_of_products):
    assert group_of_products.name == "Smartphones"
    assert group_of_products.description == "Best smartphones in country"
    assert group_of_products.products == [test_product]
    assert group_of_products.category_count == 1
    assert len(group_of_products.products) == 1
