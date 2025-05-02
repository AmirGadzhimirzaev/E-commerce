import pytest

from src.lawn_grass import LawnGrass
from tests.test_smartphone import smartphone


@pytest.fixture
def lawn_grass():
    lawn_grass_1 = LawnGrass(
        "test_name_1", "test_description_1", 25_000, 5, "test_country_1", "test_germination_period_1", "test_color_1"
    )
    lawn_grass_2 = LawnGrass(
        "test_name_2", "test_description_2", 15_000, 10, "test_country_2", "test_germination_period_2", "test_color_2"
    )
    return lawn_grass_1, lawn_grass_2


def test_lawn_grass(lawn_grass, smartphone):
    assert lawn_grass[0].name == "test_name_1"
    assert lawn_grass[0].description == "test_description_1"
    assert lawn_grass[0].price == 25_000
    assert lawn_grass[0].quantity == 5
    assert lawn_grass[0].country == "test_country_1"
    assert lawn_grass[0].germination_period == "test_germination_period_1"
    assert lawn_grass[0].color == "test_color_1"
    assert lawn_grass[0] + lawn_grass[1] == 275000

    with pytest.raises(TypeError) as er_info:
        smartphone[0] + lawn_grass[0]

    assert issubclass(er_info.type, TypeError)
