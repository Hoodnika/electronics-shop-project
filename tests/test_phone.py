import pytest

from src.phone import Phone


def test_number_of_sim():
    samsung = Phone("samsung", 50000, 10, 2)
    assert samsung.number_of_sim == 2
    with pytest.raises(ValueError):
        samsung.number_of_sim = 0
    samsung.number_of_sim = 4
    assert samsung.number_of_sim == 4

def test_repr():
    samsung = Phone("samsung", 50000, 10, 2)
    assert repr(samsung) == "Phone('samsung', 50000, 10, 2)"
