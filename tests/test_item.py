import pytest
from src.item import Item
"""Здесь надо написать тесты с использованием pytest для модуля item."""

def test_string_to_number():
    assert Item.string_to_number("5") == 5
    assert Item.string_to_number("5.0") == 5
    assert Item.string_to_number("7.5") == 7
    with pytest.raises(ValueError):
        Item.string_to_number("word")

def test_instantiate_from_csv():
    assert Item.instantiate_from_csv("src/items.csv")[0].name == "Смартфон"

def test_calculate_total_price():
    dekstop = Item("Ноутбук", 50000, 3)
    assert dekstop.calculate_total_price() == 150000

def test_apply_discount():
    dekstop2 = Item("Ноутбук", 50000, 3)
    Item.pay_rate = 0.9
    assert dekstop2.apply_discount() == 45000