import csv
import os


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    @classmethod
    def instantiate_from_csv(cls, file = '../src/broken_items.csv'):
        """
        класс-метод, инициализирующий экземпляры класса Item данными из файла 'file'.csv
        """
        try:
            cls.all = []
            with open(file, encoding="cp1251") as f:
                reader = csv.DictReader(f)
                for item in reader:
                    cls.all.append(cls(item['name'], item['price'], item['quantity']))
            return cls.all
        except KeyError:
            raise InstantiateCSVError
        except FileNotFoundError:
            raise FileNotFoundError(f'Отсутствует файл item.csv')

    @staticmethod
    def string_to_number(num_str):
        """
        статический метод, возвращающий число из числа-строки
        """
        num = float(num_str)
        num = int(num)
        return num

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity
        super().__init__()

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.__name}', {self.price}, {self.quantity})"

    def __str__(self):
        return f"{self.__name}"

    def __add__(self, other):
        if issubclass(other.__class__, Item):
            return self.quantity + other.quantity
        else:
            raise ValueError('Складывать можно только телефоны и предметы')

    @property
    def name(self):
        """
        Getter для атрибута name
        """
        return self.__name

    @name.setter
    def name(self, new_name):
        """
        Setter для атрибута name с максимальным кол-во символов в 10
        """
        self.__name = new_name[0:10]

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        total = self.price * self.quantity
        return total

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price = self.price * Item.pay_rate
        return self.price

class InstantiateCSVError(Exception):

    def __inin__(self):
        pass

    def __str__(self):
        return 'Файл item.csv поврежден'