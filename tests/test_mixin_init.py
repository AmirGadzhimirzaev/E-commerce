from src.product import Product


def test_mixin_init(capsys):
    Product("name_test_1", "description_test_1", 10_500, 4)
    message = capsys.readouterr()
    assert message.out.strip() == "Product('name_test_1', 'description_test_1', 10500, 4)"
