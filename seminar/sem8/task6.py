# Напишите функцию, которая преобразует pickle файл хранящий список словарей в табличный csv файл.
# Для тестирования возьмите pickle версию файла из задачи 5 этого семинара.
# Функция должна извлекать ключи словаря для заголовков столбца из переданного файла.

import csv
from pathlib import Path
import pickle

__all__ = ['pickle_2_csv']

def pickle_2_csv(path: Path) -> None:
    with (
        open(path, 'rb') as f_r,
        open(f'{path.stem}.csv', 'w', newline='', encoding='utf-8') as f_w
    ):
        data = pickle.load(f_r)
        keys = data[0].keys()
        csv_writer = csv.DictWriter(f_w, fieldnames=keys, dialect='excel-tab', quoting=csv.QUOTE_NONNUMERIC)
        csv_writer.writeheader()  # writeheader() - записывает заголовки
        csv_writer.writerows(data)


if __name__ == '__main__':
    pickle_2_csv(Path('new_users.pickle'))
