from src.item import Item

item1 = Item("Смартфон", 10000, 20)

if __name__ == '__main__':

    assert item1.calculate_total_price == 200000
