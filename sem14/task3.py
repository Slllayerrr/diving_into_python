# Напишите для задачи 1 тесты unittest. Проверьте следующие варианты:
# возврат строки без изменений
# возврат строки с преобразованием регистра без потери символов
# возврат строки с удалением знаков пунктуации
# возврат строки с удалением букв других алфавитов
# возврат строки с учётом всех вышеперечисленных пунктов (кроме п. 1)
import unittest
from string import ascii_letters

def del_symbol(text: str) -> str:
    return ''.join(char for char in text if char in ascii_letters + ' ').lower()


class TestCaseName(unittest.TestCase):
    def test_original_str(self):
        self.assertEqual('hello world', del_symbol('hello world'), 'Str not cange')

    def test_lower(self):
        self.assertEqual('hello world', del_symbol('Hello World'), 'Str is not lowwer')

    def test_punctuation(self):
        self.assertEqual('hello world', del_symbol('h@ello w%%&&&&&!!!!!!orld'), 'Str with punctuation')

    def test_lang(self):
        self.assertEqual('hello world', del_symbol('hello worldаоаоаоанананан'), 'Str with punctuation')

    def test_ll(self):
        self.assertEqual('hello world', del_symbol('Helloмамама!!!!* World'), 'All text')



if __name__ == '__main__':
    unittest.main(verbosity=2)