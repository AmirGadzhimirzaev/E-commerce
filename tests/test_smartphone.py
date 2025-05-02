import pytest

from src.product import Product
from src.smartphone import Smartphone


@pytest.fixture
def smartphone():
    smart_1 = Smartphone("name_test_1", "description_test_1", 10000, 5, 11.5, "10", 256, "red")
    smart_2 = Smartphone("name_test_2", "description_test_2", 20000, 8, 51.5, "30", 512, "black")
    return smart_1, smart_2


def test_smartphones(smartphone):
    assert smartphone[0].name == "name_test_1"
    assert smartphone[0].description == "description_test_1"
    assert smartphone[0].price == 10000
    assert smartphone[0].quantity == 5
    assert smartphone[0].efficiency == 11.5
    assert smartphone[0].model == "10"
    assert smartphone[0].memory == 256
    assert smartphone[0].color == "red"
    assert smartphone[0] + smartphone[1] == 210000
    assert issubclass(type(smartphone[0]), Product) == True
