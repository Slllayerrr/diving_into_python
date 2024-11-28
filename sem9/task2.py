# Дорабатываем задачу 1.
# Превратите внешнюю функцию в декораторе.
# Он должен проверять входят ли переданные в функцию угадайку числа в диапазоны [1, 100] и [1, 10].
# Если не входят, вызывать функцию со случайными числами
# из диапазонов.
from typing import Callable
from random import randint


def guess_num(func):
    MIN_NUM = 1
    MAX_NUM = 100
    MIN_CNT = 1
    MAX_CNT = 10

    def wrapper(num: int, cnt: int):
        if num < MIN_NUM or num > MAX_NUM:
            num = randint(MIN_NUM, MAX_NUM)
        if cnt < MIN_CNT or cnt > MAX_CNT:
            cnt = randint(MIN_CNT, MAX_CNT)
            print(f'У нас {cnt} попыток')
        return func(num, cnt)

    return wrapper


@guess_num
def guess_game(num: int, cnt: int):
    for i in range(1, cnt + 1):
        print(f'Попытка: {i}')
        user_input = int(input('Введите число от 1 до 100: '))
        if num == user_input:
            print(f'Число отгадано с {i} попытки')
            return
        elif num > user_input:
            print('Ваше число меньше загаданного')
        elif num < user_input:
            print('Ваше число больше загаданного')
    else:
        print(f'Загаданное число: {num}, кол-во попыток: {cnt}')




if __name__ == '__main__':
    guess_game(150, 110)
