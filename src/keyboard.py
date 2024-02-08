from src.item import Item


class Lang:
    """
    Хранит информацию раскладки клавиатуры
    """
    def __init__(self):
        self.__language = "EN"

    @property
    # добавит геттер атрибутa `language`
    def language(self):
        return self.__language

    def change_lang(self):
        # изменяет раскладку клавиатуры
        if self.__language == "EN":
            self.__language = "RU"
        else:
            self.__language = "EN"


class Keyboard(Item, Lang):
    """
    Класс содержит информацию о товаре "клавиатура"
    @param name: название
    @param price: цена
    @param quantity: количество
    """
    def __init__(self, name: str, price: float, quantity: int, ):
        # вызывает информацию о клавиатуре из класса Item
        super().__init__(name, price, quantity)
        Lang.__init__(self)

    def __str__(self):
        # выводит информацию о клавиатуре
        return self.name
