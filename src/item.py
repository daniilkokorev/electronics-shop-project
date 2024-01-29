import csv


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара. сделать приватным
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity
        Item.all.append(self)

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price * self.quantity

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= self.pay_rate

    @property
    # добавит геттер атрибутa `name`
    def name(self):
        return self.__name

    @name.setter
    # добавит сеттер для `name`
    # проверяет длину наименования товара не более 10 символов
    def name(self, name):
        if len(name) > 10:
            self.__name = name[:10]
        else:
            self.__name = name

    @classmethod
    # получение данных экземпляра класса из csv файла
    def instantiate_from_csv(cls, csv_file):
        cls.all = []
        with open(csv_file, newline='', encoding='windows-1251') as f:
            file_item = csv.DictReader(f)
            for item in file_item:
                cls(str(item["name"]), float(item["price"]), int(item["quantity"]))

    @staticmethod
    # возвращающий число из строки
    def string_to_number(str_number):
        return int(float(str_number))

    def __repr__(self):
        # метод выводит имя класса и объекты класса для разработчика
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity})"

    def __str__(self):
        # метод выводит объект класса для пользователя
        return str(self.name)
