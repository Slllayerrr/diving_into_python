# Напишите функцию, которая ищет json файлы в указанной директории и сохраняет их содержимое в виде одноимённых pickle файлов.

import json
from pathlib import Path
import pickle

__all__ = ['json_to_pickle']

def json_to_pickle(input_file: Path) -> None:
    for obj in input_file.iterdir():
        if obj.is_file() and obj.suffix == '.json':
            with open(obj, 'r', encoding='utf-8') as f_r:
                data = json.load(f_r)
            with open(f'{obj.stem}.pickle', 'wb') as f_wb:
                pickle.dump(data, f_wb)


if __name__ == '__main__':
    json_to_pickle(Path.cwd())
