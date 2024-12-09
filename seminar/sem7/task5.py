# ✔ Доработаем предыдущую задачу.
# ✔ Создайте новую функцию которая генерирует файлы с разными расширениями.
# ✔ Расширения и количество файлов функция принимает в качестве параметров.
# ✔ Количество переданных расширений может быть любым.
# ✔ Количество файлов для каждого расширения различно.

from random import randint, choices
from string import ascii_lowercase, digits


def create_file(
        expansion: str = 'bin',
        min_len: int = 6,
        max_len: int = 30,
        min_b: bytes = 256,
        max_b: bytes = 4096,
        count_file: int = 2
) -> None:
    for _ in range(count_file):
        name = ''.join(choices(ascii_lowercase + digits + '_', k=randint(min_len, max_len)))
        data = bytes(randint(0, 255) for _ in range(randint(min_b, max_b)))
        with open(f'{name}.{expansion}', 'wb') as file:
            file.write(data)


def gen_files(**kwargs):
    for exp, count in kwargs.items():
        create_file(expansion=exp, count_file=count)


if __name__ == '__main__':
    gen_files(jpg=1, txt=2, bin=1)
