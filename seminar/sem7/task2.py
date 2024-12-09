# ✔ Напишите функцию, которая генерирует псевдоимена.
# ✔ Имя должно начинаться с заглавной буквы, состоять из 4-7 букв, среди которых обязательно должны быть гласные.
# ✔ Полученные имена сохраните в файл.
import random
import string
from pathlib import Path
from random import choice

__all__ = ['random_name_file']
MIN_LIMIT = 4
MAX_LIMIT = 7

# 1 вариант решения
# def random_name_file(cnt_str: int, file_name: str | Path):
#     count = 0
#     while count < cnt_str:
#         size = random.randint(MIN_LIMIT, MAX_LIMIT)
#         name = ''.join(random.choices(string.ascii_letters, k=size)).title()
#         with open(file_name, 'a', encoding='UTF-8') as file:
#             for i in name:
#                 if i == "a" or i == "e" or i == "i" or i == "o" or i == "u" or i == "y":
#                     file.write(f'{name}\n')
#                     count += 1
#                     break
#
#
# random_name_file(10, 'ramdon_name.txt')

# 2 вариант решения
VOWELS = 'eyuioa'
CONSTANTS = 'qwrtpsdfghjklzxcvbnm'


def random_name_file(cnt_str: int, file_name: str | Path):
    for _ in range(cnt_str):
        first_chr = choice([-1, 1])
        name = ''
        for _ in range(random.randint(MIN_LIMIT, MAX_LIMIT)):
            if first_chr == -1:
                name += choice(CONSTANTS)
            else:
                name += choice(VOWELS)
            first_chr *= -1

        with open(file_name, 'a', encoding='UTF-8') as f:
            f.write(name.title() + '\n')


# 3 вариант решения
#
# def random_name_file(cnt_str: int, file_name: str | Path):
#     for _ in range(cnt_str):
#         name = ''.join(choice(VOWELS) if i in (2, 4, 6) else choice(CONSTANTS)
#                        for i in range(random.randint(MIN_LIMIT, MAX_LIMIT)))
#         with open(file_name, 'a', encoding='UTF-8') as f:
#             f.write(name.title() + '\n')
#
#
# random_name_file(10, 'ramdon_name.txt')

if __name__ == '__main__':
    random_name_file(10, 'ramdon_name.txt')
