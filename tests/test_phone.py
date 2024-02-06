from src.phone import Phone
import pytest


@pytest.fixture
def phone1():
    return Phone("iPhone 14", 120_000, 5, 2)


def test_number_of_sim(phone1):
    # проверяет соответствующее количество сим карт в телефоне
    phone1.number_of_sim = 3
    assert phone1.number_of_sim == 3
    with pytest.raises(ValueError):
        phone1.number_of_sim = 0


def test_repr_metod(phone1):
    # проверяет вывод метода информации для программиста
    assert repr(phone1) == "Phone('iPhone 14', 120000, 5, 2)"
