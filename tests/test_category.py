import pytest

from src.category import Category
from src.product import Product


@pytest.fixture
def category():
    test_product_1 = Product("test_name_1", "test_description_1", 5, 10)
    test_product_2 = Product("test_name_2", "test_description_2", 10, 50)

    return test_product_1, test_product_2


def test_category_init(category):
    category_1 = Category("a", "b", [category[0]])

    assert category_1.name == "a"
    assert category_1.description == "b"
    assert category_1.products == "test_name_1, 5 руб. Остаток: 10 шт.\n"

    category_1.add_product(category[1])

    assert category_1.products == "test_name_1, 5 руб. Остаток: 10 шт.\ntest_name_2, 10 руб. Остаток: 50 шт.\n"
    assert str(category_1) == "a, количество продуктов: 10 шт."

    with pytest.raises(TypeError) as er_info:
        category_1.add_product("Not a product test")

    assert issubclass(er_info.type, TypeError)


def test_category_counters():
    current_category_count = Category.category_count
    current_product_count = Category.product_count
    product_1 = Product("a", "b", 1, 2)
    product_2 = Product("c", "d", 3, 4)
    Category("new", "category", [product_1, product_2])

    assert Category.category_count == current_category_count + 1
    assert Category.product_count == current_product_count + 2


def test_category_exception(category):
    category_1 = Category("test_name_1", "test_description_1", [])
    category_2 = Category("test_2", "test_2", [category[0], category[1]])

    assert category_1.middle_price() == 0
    assert category_2.middle_price() == 7.5
