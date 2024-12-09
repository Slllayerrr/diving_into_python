# Напишите следующие функции:
# ○ Нахождение корней квадратного уравнения
# ○ Генерация csv файла с тремя случайными числами в каждой строке. 100-1000 строк.
# ○ Декоратор, запускающий функцию нахождения корней квадратного уравнения с каждой тройкой чисел из csv файла.
# ○ Декоратор, сохраняющий переданные параметры и результаты работы функции в json файл.
from functools import wraps
from random import randint
from typing import Callable
from pathlib import Path
import json
import csv
__all__ = ['generate_csv_file', 'save_to_json', 'square_roots']

def generate_csv_file(func: Callable):
    MAX_LIMIT = 1000
    MIN_LIMIT = 100
    rows_int = randint(MIN_LIMIT, MAX_LIMIT)
    rows = []
    for _ in range(rows_int):
        a = randint(1, MAX_LIMIT)
        b = randint(1, MAX_LIMIT)
        c = randint(1, MAX_LIMIT)
        rows.append({a, b, c})

    with open(f'{func.__name__}.csv', 'w', newline='', encoding='utf-8') as f:
        csv_write = csv.writer(f, dialect='excel-tab')
        for list_dict in rows:
            csv_write.writerow(list_dict)

    @wraps(func)
    def wrapper(a, b, c):
        data = []
        with open(f'{func.__name__}.csv', 'r', newline='', encoding='utf-8') as f:
            csv_reader = csv.reader(f, dialect='excel-tab')
            for i in csv_reader:
                a = int(i[0])
                b = int(i[1])
                c = int(i[2])
                dicts = {}
                dicts['a'] = a
                dicts['b'] = b
                dicts['c'] = c
                dicts['result'] = func(a, b, c)
                data.append(dicts)
            return data
    return wrapper


def save_to_json(func: Callable):
    file = Path(f'{func.__name__}.json')
    if file.is_file():
        with open(file, 'r', encoding='utf-8') as f_r:
            list_of_dicts = json.load(f_r)
    else:
        list_of_dicts = []

    @wraps(func)
    def wrapper(a, b, c):
        result = func(a, b, c)
        json_dict = {'a': a, 'b': b, 'c': c, 'result': result}
        list_of_dicts.append(json_dict)
        with open(file, 'w', encoding='utf-8') as f:
            json.dump(list_of_dicts, f)
        return result

    return wrapper

@generate_csv_file
@save_to_json
def square_roots(a, b, c):
    d = b ** 2 - 4 * a * c
    if d > 0:
        x1 = (-b + d ** 0.5) / (2 * a)
        x2 = (-b - d ** 0.5) / (2 * a)
        return x1, x2
    elif d == 0:
        x = -b / (2 * a)
        return x
    else:
        return None

if __name__ == '__main__':
    square_roots(1, 8, 12)