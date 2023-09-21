import csv
import os
class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    @classmethod
    def instantiate_from_csv(cls, file):
        """
        класс-метод, инициализирующий экземпляры класса Item данными из файла 'file'.csv
        """
        cls.all = []
        file_lst_path = file.split("/")
        with open(os.path.join("..", file_lst_path[0], file_lst_path[1]), encoding="cp1251") as f:
            reader = csv.DictReader(f)
            for item in reader:
                cls.all.append(cls(item['name'], item['price'], item['quantity']))
        return cls.all

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
        # self.all.append(self)


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

        # self.__name = name[0:10]

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



