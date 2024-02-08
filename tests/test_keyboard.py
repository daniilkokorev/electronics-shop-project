from src.keyboard import Keyboard
import pytest


@pytest.fixture
def kb():
    return Keyboard('Dark Project KD87A', 9600, 5)


def test_str_metod(kb):
    # проверяет вывод информации о клавиатуре
    assert str(kb) == "Dark Project KD87A"


def test_change_lang(kb):
    # проверяет раскладку клавиатуры и изменение языка
    assert str(kb.language) == "EN"
    kb.change_lang()
    assert str(kb.language) == "RU"
    # Сделали EN -> RU -> EN
    kb.change_lang()
    assert str(kb.language) == "EN"
    with pytest.raises(AttributeError):
        kb.language = 'CH'
