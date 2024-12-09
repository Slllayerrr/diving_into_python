# Создайте функцию аналог get для словаря.
# Помимо самого словаря функция принимает ключ и значение по умолчанию.
# При обращении к несуществующему ключу функция должна возвращать дефолтное значение.
# Реализуйте работу через обработку исключений.
import unittest

class TestFactorial(unittest.TestCase):

    def test_get_defolt_value(self):
        self.assertEqual(my_get({1: 'hello', 2: 'wrld'}, 5, 'Такого значения нет'), 'Такого значения нет')

    def test_get_defolt_value_none(self):
        self.assertEqual(my_get({1: 'hello', 2: 'wrld'}, 10), None)

    def test_get_value(self):
        self.assertEqual(my_get({1: 'hello', 2: 'wrld'}, 1), 'hello')


def my_get(my_dict, key, defolt_value=None):
    res = defolt_value
    try:
        res = my_dict[key]
    except KeyError:
        pass
    return res

if __name__ == '__main__':
    unittest.main(verbosity=2)