# Улучшаем задачу 2.
# � Добавьте возможность запуска функции “угадайки” из модуля в командной строке терминала.
# � Строка должна принимать от 1 до 3 аргументов: параметры вызова функции.
# � Для преобразования строковых аргументов командной строки в числовые параметры используйте генераторное выражение.

import random
from sys import argv

__all__ = ['guess']


def guess(low_limit: int = 0, up_limit: int = 100, count: int = 10) -> bool:
    number = random.randint(low_limit, up_limit)
    for _ in range(count):
        anser = int(input("Введите число: "))
        if anser == number:
            return True
        elif anser > number:
            print(f"Число {anser} больше загаданного")
        else:
            print(f"Число {anser} меньше загаданного")
    else:
        return False


if __name__ == '__main__':
    params = argv[1:]
    params = (int(number) for number in params)
    print(guess(*params))
