# Напишите для задачи 1 тесты doctest. Проверьте следующие варианты:
# возврат строки без изменений
# возврат строки с преобразованием регистра без потери символов
# возврат строки с удалением знаков пунктуации
# возврат строки с удалением букв других алфавитов
# возврат строки с учётом всех вышеперечисленных пунктов (кроме п. 1)
from string import ascii_letters

def del_symbol(text: str) -> str:
    """
    >>> del_symbol('hello world')
    'hello world'

    >>> del_symbol('Hello World')
    'hello world'

    >>> del_symbol('hello world!!!!')
    'hello world'

    >>> del_symbol('hello worldирмир')
    'hello world'

    >>> del_symbol('HELLOФВЧЧ #&&&&$worldирмир!')
    'hello world'
    """
    return ''.join(char for char in text if char in ascii_letters + ' ').lower()

if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)