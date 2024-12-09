# Напишите для задачи 1 тесты pytest. Проверьте следующие варианты:
# возврат строки без изменений
# возврат строки с преобразованием регистра без потери символов
# возврат строки с удалением знаков пунктуации
# возврат строки с удалением букв других алфавитов
# возврат строки с учётом всех вышеперечисленных пунктов (кроме п. 1)
from string import ascii_letters

import pytest


def del_symbol(text: str) -> str:
    return ''.join(char for char in text if char in ascii_letters + ' ').lower()


def test_original_str():
    assert del_symbol('hello world') == 'hello world'


def test_lower():
    assert del_symbol('Hello World') == 'hello world'


def test_punctuation():
    assert del_symbol('h@ello w%%&&&&&!!!!!!orld') == 'hello world'


def test_lang():
    assert del_symbol('hello worldаоаоаоанананан') == 'hello world'


def test_all():
    assert del_symbol('Helloмамама!!!!* World') == 'hello world'


if __name__ == '__main__':
    pytest.main(['-vv'])
