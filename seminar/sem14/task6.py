# На семинаре 13 был создан проект по работе с пользователями (имя, id, уровень).
# Напишите 3-7 тестов pytest для данного проекта.
# Используйте фикстуры.
import json
from pathlib import Path
import pytest

@pytest.fixture
def new_set():
    data = {
        User('vfvf', 1, 2),
        User('rgg', 2, 2),
        User('vova', 3, 2),
        User('katy', 12, 5)
    }
    return data

@pytest.fixture
def new_user(new_set):
    return User('New', 1101, 5)

@pytest.fixture
def good_user(new_set):
    return User('vova', 3, 2)

def test_load(new_set):
    project = Project()
    result = project.read_file(Path(r'C:\Users\User\Desktop\diving_into_python\sem8\users.json'))
    assert new_set == result

def test_enter(good_user):
    project = Project()
    project.read_file(Path(r'C:\Users\User\Desktop\diving_into_python\sem8\users.json'))
    result = project.enter_user('vova', 3)
    assert result == good_user

def test_no_enter():
    project = Project()
    project.read_file(Path(r'C:\Users\User\Desktop\diving_into_python\sem8\users.json'))
    with pytest.raises(AccessError):
        project.enter_user('TTTT', 2)

def test_add_user(new_user):
    project= Project()
    project.read_file(Path(r'C:\Users\User\Desktop\diving_into_python\sem8\users.json'))
    project.enter_user('vova', 3)
    result = project.add_user('New', 1101, 5)
    assert result == new_user

def test_not_add_user(new_user):
    project= Project()
    project.read_file(Path(r'C:\Users\User\Desktop\diving_into_python\sem8\users.json'))
    project.enter_user('vova', 3)
    with pytest.raises(LevelError):
        project.add_user('New', 1101, 1)






class UserException(Exception):
    pass


class LevelError(UserException):
    pass


class AccessError(UserException):
    pass


class User:
    def __init__(self, name, user_id, level):
        self.name = name
        self.user_id = user_id
        self.level = level

    def __str__(self):
        return f'{self.name= }, {self.user_id= }, {self.level= }'

    def __eq__(self, other):
        return self.name == other.name and self.user_id == other.user_id

    def __hash__(self):
        return hash((str(self.name), str(self.user_id)))


class Project:
    def __init__(self):
        self.user = None
        self.users = set()

    def read_file(self, file: Path) -> set[User]:
        with open(file, 'r', encoding='utf-8') as f:
            read_json = json.load(f)

        for level, value_dict in read_json.items():
            for user_id, user_name in value_dict.items():
                self.users.add(User(user_name, int(user_id), int(level)))
        return self.users

    def enter_user(self, name, user_id):
        current_user = User(name, user_id, 0)
        if current_user not in self.users:
            raise AccessError('В доступе отказано')

        for user in self.users:
            if user == current_user:
                self.user = user
                return self.user

    def add_user(self, name, user_id, level):
        if level < self.user.level:
            raise LevelError('Уровень меньше чем наш')
        new_user = User(name, user_id, level)
        self.users.add(new_user)
        return new_user


if __name__ == '__main__':
    pytest.main(['-vv'])