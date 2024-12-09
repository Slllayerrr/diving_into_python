# Прочитайте созданный в прошлом задании csv файл без использования csv. DictReader.
# Распечатайте его как pickle строку.

import csv
import pickle
from pathlib import Path

__all__ = ['cvs_to_pickle']

def cvs_to_pickle(file_name: Path) -> None:
    pickle_list = []
    with open(file_name, 'r', newline='', encoding='utf-8') as f_p:
        csv_reader = csv.reader(f_p, dialect='excel-tab')
        for i, row in enumerate(csv_reader):
            if i == 0:
                pickle_keys = row
            else:
                pickle_dict = dict(zip(pickle_keys, row))
                pickle_list.append(pickle_dict)
    print(pickle.dumps(pickle_list))


if __name__ == '__main__':
    cvs_to_pickle('new_users.csv')