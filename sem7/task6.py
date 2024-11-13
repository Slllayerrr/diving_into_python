# ✔ Дорабатываем функции из предыдущих задач.
# ✔ Генерируйте файлы в указанную директорию — отдельный параметр функции.
# ✔ Отсутствие/наличие директории не должно вызывать ошибок в работе функции (добавьте проверки).
# ✔ Существующие файлы не должны удаляться/изменяться в случае совпадения имён.
from os import mkdir
from random import randint, choices
from string import ascii_lowercase, digits
from pathlib import Path
from os import chdir


def create_file(
        expansion: str = 'bin',
        min_len: int = 6,
        max_len: int = 30,
        min_b: bytes = 256,
        max_b: bytes = 4096,
        count_file: int = 2
) -> None:
    for _ in range(count_file):
        while True:
            name = ''.join(choices(ascii_lowercase + digits + '_', k=randint(min_len, max_len)))
            name = f'{name}.{expansion}'
            if not Path(name).is_file():  # проверка существует ли файл
                break
        data = bytes(randint(0, 255) for _ in range(randint(min_b, max_b)))
        with open(name, 'wb') as file:
            file.write(data)


def gen_files(path: str | Path, **kwargs):
    if isinstance(path, str):
        path = Path(path)
    if not path.is_dir():
        path.mkdir(parents=True)
    chdir(path)

    for exp, count in kwargs.items():
        create_file(expansion=exp, count_file=count)


if __name__ == '__main__':
    gen_files(r'C:\Users\User\Desktop\diving_into_python\sem7\NEW', jpg=1, txt=2, bin=1)
