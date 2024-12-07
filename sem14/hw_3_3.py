import pytest


def my_get(my_dict, key, defolt_value=None):
    res = defolt_value
    try:
        res = my_dict[key]
    except KeyError:
        pass
    return res


def test_get_defolt_value():
    assert my_get({1: 'hello', 2: 'wrld'}, 5, 'Такого значения нет') == 'Такого значения нет'


def test_get_defolt_value_none():
    assert my_get({1: 'hello', 2: 'wrld'}, 10) == None


def test_get_value():
    assert my_get({1: 'hello', 2: 'wrld'}, 1) == 'hello'


if __name__ == '__main__':
    pytest.main(['-vv'])
