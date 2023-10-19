from src.item import Item
from abc import ABC, abstractmethod


class LayoutMixin:
    Language = "EN"

    def __init__(self):
        self.__language = self.Language

    def change_lang(self):
        if self.__language == "EN":
            self.__language = "RU"
        else:
            self.__language = "EN"

    @property
    def language(self):
        return self.__language

class Keyboard(Item, LayoutMixin):

    def __init__(self, name: str, price: float, quantity: int) -> None:
        super().__init__(name, price, quantity)


