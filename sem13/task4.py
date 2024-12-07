# Вспоминаем задачу из семинара 8 про сериализацию данных, где в бесконечном цикле запрашивали имя, личный
# идентификатор и уровень доступа (от 1 до 7) сохраняя информацию в JSON файл.
# Напишите класс пользователя, который хранит эти данные в свойствах экземпляра.
# Отдельно напишите функцию, которая считывает информацию из JSON файла и формирует множество пользователей.



import json
from pathlib import Path


class User:
    def __init__(self,user_id, name, level):
        self.name = name
        self.user_id = user_id
        self.level = level

    def __str__(self):
        return f'{self.name=}, {self.level=}, {self.user_id=}'

def read_file(file: Path)-> set[User]:
    with open(file, 'r', encoding='utf-8') as f:
        read_json = json.load(f)
    users = set()
    for level, value_dict in read_json.items():
        for user_id, user_name in value_dict.items():
            users.add(User(user_id, user_name, level))
    return users


if __name__ == '__main__':
    print(*read_file(Path(r'C:\Users\User\Desktop\diving_into_python\sem8\users.json')), sep='\n')
