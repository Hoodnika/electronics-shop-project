import pytest
from src.keyboard import Keyboard

def test_chanhe_lang():
    kb = Keyboard("saske",228, 1)
    assert kb.language == "EN"
    kb.change_lang()
    assert kb.language == "RU"
    kb.change_lang()
    assert kb.language == "EN"
    with pytest.raises(AttributeError):
        kb.language = "CH"