# ✔ Напишите функцию, которая заполняет файл (добавляет в конец) случайными парами чисел.
# ✔ Первое число int, второе - float разделены вертикальной чертой.
# ✔ Минимальное число - -1000, максимальное - +1000.
# ✔ Количество строк и имя файла передаются как аргументы функции.
import random
from pathlib import Path

MIN_LIMIT = -1000
MAX_LIMIT = 1000


def randon_append_file(cnt_str: int, file_name: str | Path) -> None:
    with open(file_name, 'a', encoding='UTF-8') as file:
        for _ in range(cnt_str):
            int_num = random.randint(MIN_LIMIT, MAX_LIMIT)
            float_num = random.uniform(MIN_LIMIT, MAX_LIMIT)
            file.write(f'{int_num:>4}  |  {float_num}\n')


randon_append_file(10, 'random_numbers.txt')
