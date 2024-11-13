# Напишите функцию группового переименования файлов. Она должна:
# ✔ принимать параметр желаемое конечное имя файлов. При переименовании в конце имени добавляется порядковый номер.
# ✔ принимать параметр количество цифр в порядковом номере.
# ✔ принимать параметр расширение исходного файла. Переименование должно работать только для этих файлов внутри каталога.
# ✔ принимать параметр расширение конечного файла.
# ✔ принимать диапазон сохраняемого оригинального имени. Например, для диапазона [3, 6] берутся буквы с 3 по 6 из исходного имени файла.
# К ним прибавляется желаемое конечное имя, если оно передано. Далее счётчик файлов и расширение.

from os import chdir
from pathlib import Path


def rename_files(
        path: Path,
        desired_name: str,
        num_digit: int,
        expan_old: str,
        expan_new: str,
        range_lst: list[int]
) -> None:
    chdir(path)
    count = 0
    for file in path.iterdir():
        fl_name = file.name
        range_name = ''
        if file.is_file() and file.suffix in expan_old:
            for i in range(range_lst[0], range_lst[1]):
                range_name += fl_name[i]
            count += 1
            Path(f'{file.name}').rename(f'{range_name}{desired_name}{str(count).zfill(num_digit)}{expan_new}')

if __name__ == '__main__':
    rename_files(Path(r'C:\Users\User\Desktop\diving_into_python\sem7'), '_NEW_', 3, '.doc', '.txt', [3, 6])
