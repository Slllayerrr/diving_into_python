# Напишите функцию, которая в бесконечном цикле запрашивает имя, личный идентификатор и уровень доступа (от 1 до 7).
# После каждого ввода добавляйте новую информацию в JSON файл.
# Пользователи группируются по уровню доступа.
# Идентификатор пользователя выступает ключём для имени.
# Убедитесь, что все идентификаторы уникальны независимо от уровня доступа.
# При перезапуске функции уже записанные в файл данные должны сохраняться.

import json
from pathlib import Path

__all__ = ['set_users']

def set_users(user_file: Path) -> None:
    uniq_id = set()
    if not user_file.is_file():
        data = {str(i): {} for i in range(1, 7 + 1)}
    else:
        with open(user_file, 'r', encoding='utf-8') as file:
            data = json.load(file)

            for dict_level in data.values():
                uniq_id.update(dict_level)

    while True:
        name = input('Введите имя: ')
        if not name:
            break
        user_id = input('Введите id: ')
        level = input('Введите уровень от 1 до 7: ')
        while level not in ('1', '2', '3', '4', '5', '6', '7'):
            print('Некорректный ввод! Уровень доступа от 1 до 7!')
            level = input('Введите уровень от 1 до 7: ')
        if user_id not in uniq_id:
            data[level].update({user_id: name})
            # data[level][user_id] = name   - 2 вариант
            uniq_id.add(user_id)
            with open(user_file, 'w', encoding='utf-8') as file:
                json.dump(data, file, indent=4, ensure_ascii=False)


if __name__ == '__main__':
    set_users(Path('users.json'))
