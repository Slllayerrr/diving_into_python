# Напишите декоратор, который сохраняет в json файл параметры декорируемой функции и результат, который она возвращает.
# При повторном вызове файл должен расширяться, а не перезаписываться.
# Каждый ключевой параметр сохраните как отдельный ключ json словаря.
# Для декорирования напишите функцию, которая может принимать как позиционные, так и ключевые аргументы.
# Имя файла должно совпадать с именем декорируемой функции.

import json
from pathlib import Path
from typing import Callable


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


@save_to_json
def get_all(*args, **kwargs):
    return args

if __name__ == '__main__':
    get_all(5, 34, 44, 'vfvf', a=12, b=32,c=34)