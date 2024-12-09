# � Создайте модуль с функцией внутри.
# � Функция принимает на вход три целых числа: нижнюю и верхнюю границу и количество попыток.
# � Внутри генерируется случайное число в указанных границах
# и пользователь должен угадать его за заданное число попыток.
# � Функция выводит подсказки “больше” и “меньше”.
# � Если число угадано, возвращается истина, а если попытки исчерпаны - ложь.

import random

def guess(low_limit: int=0, up_limit: int=100, count: int=10) -> bool:
    number = random.randint(low_limit, up_limit+1)
    n = 0
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
    print(guess())