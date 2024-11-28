# Объедините функции из прошлых задач.
# Функцию угадайку задекорируйте:
# ○ декораторами для сохранения параметров,
# ○ декоратором контроля значений и
# ○ декоратором для многократного запуска.
# Выберите верный порядок декораторов.

from random import randint
from typing import Callable
from pathlib import Path
import json


def save_to_json(func: Callable):
    file = Path(f'{func.__name__}.json')
    if file.is_file():
        with open(file, 'r', encoding='utf-8') as f_r:
            list_of_dicts = json.load(f_r)
    else:
        list_of_dicts = []

    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        json_dict = {'arg': args, **kwargs, 'result': result}
        list_of_dicts.append(json_dict)
        with open(file, 'w', encoding='utf-8') as f:
            json.dump(list_of_dicts, f)
        return result

    return wrapper


def deco_count(num: int):
    def deco(func: Callable):
        counter = []

        def wrapper(*args, **kwargs):
            for cnt in range(1, num + 1):
                print(f'Функцию запустили {cnt} раз')
                res = func(*args, **kwargs)
                counter.append(res)
            return counter

        return wrapper

    return deco


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


@deco_count(2)
@guess_num
@save_to_json
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
    guess_game(15, 3)
