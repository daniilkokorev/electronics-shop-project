from config import ITEMS
from src.item import Item
import pytest


@pytest.fixture
def item1():
    return Item("Смартфон", 10000, 20)


def test_calculate_total_price(item1):
    """Тест проверяет вычислание общей стоимоти товара"""
    assert item1.calculate_total_price() == 200000


def test_apply_discount(item1):
    """Тест проверяет стоимоть товара со скидкой"""
    item1.pay_rate = 0.8
    assert item1.price * item1.pay_rate == 8000.0


def test_instantiate_from_csv(item1):
    """Проверяет длинну списка товаров"""
    Item.instantiate_from_csv(ITEMS)
    assert len(item1.all) == 5


def test_name(item1):
    """Тест проверяет длину наименования товара не более 10 символов"""
    item1.name = "Смартфон"
    assert item1.name == "Смартфон"
    item1.name = "СуперСмартфон"
    assert item1.name == "СуперСмарт"


def test_string_to_number(item1):
    """Тест проверяет вывод числа из строки"""
    assert Item.string_to_number('5') == 5
    assert Item.string_to_number('5.0') == 5
    assert Item.string_to_number('5.5') == 5


def test_repr_metod(item1):
    assert repr(item1) == "Item('Смартфон', 10000, 20)"


def test_str_metod(item1):
    assert str(item1) == 'Смартфон'
