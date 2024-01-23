from src.item import Item

item1 = Item("Смартфон", 10000, 20)


def test_calculate_total_price():
    assert item1.calculate_total_price() == 200000


def test_apply_discount():
    assert 10000 * item1.pay_rate == item1.price
    assert item1.price == 10000
