# Создайте функцию, которая создаёт файлы с указанным расширением.
# Функция принимает следующие параметры:
# ✔ расширение
# ✔ минимальная длина случайно сгенерированного имени, по умолчанию 6
# ✔ максимальная длина случайно сгенерированного имени, по умолчанию 30
# ✔ минимальное число случайных байт, записанных в файл, по умолчанию 256
# ✔ максимальное число случайных байт, записанных в файл, по умолчанию 4096
# ✔ количество файлов, по умолчанию 2
# Имя файла и его размер должны быть в рамках переданного диапазона.
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


if __name__ == '__main__':
    create_file()
