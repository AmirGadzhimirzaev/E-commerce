from src.category import Category
from src.product import Product


def test_category_init():
    test_product_1 = Product("test_name_1", "test_description_1", 5, 100)
    test_product_2 = Product("test_name_2", "test_description_2", 5, 100)
    category = Category("a", "b", [test_product_1])

    assert category.name == "a"
    assert category.description == "b"
    assert category.products == "test_name_1, 5 руб. Остаток: 100 шт.\n"

    category.add_product(test_product_2)

    assert category.products == "test_name_1, 5 руб. Остаток: 100 шт.\ntest_name_2, 5 руб. Остаток: 100 шт.\n"


def test_category_counters():
    current_category_count = Category.category_count
    current_product_count = Category.product_count
    product_1 = Product("a", "b", 1, 2)
    product_2 = Product("c", "d", 3, 4)
    Category("new", "category", [product_1, product_2])

    assert Category.category_count == current_category_count + 1
    assert Category.product_count == current_product_count
