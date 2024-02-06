from src.item import Item


class Phone(Item):
    """
    Класс содержит информацию о товаре "телефон"

    name: модель телефона
    price: цена телефона
    quantity: количество товара
    number_of_sim: количество поддерживаемых симкарт
    """
    def __init__(self, name: str, price: float, quantity: int, number_of_sim: int):
        # вызывает информацию о телефоне из класса Item
        super().__init__(name, price, quantity)
        # добавляет информацию по количеству симкарт
        self.__number_of_sim = number_of_sim

    def __repr__(self):
        # выводит информацию по наличию телефонов
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity}, {self.number_of_sim})"

    @property
    # добавит геттер атрибутa `number_of_sim`
    def number_of_sim(self):
        return self.__number_of_sim

    @number_of_sim.setter
    def number_of_sim(self, simcard):
        # проверяет количество сим карт
        if simcard <= 0:
            raise ValueError('Количество физических SIM-карт должно быть целым числом больше нуля.')
        else:
            self.__number_of_sim = simcard
