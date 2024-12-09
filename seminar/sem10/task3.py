# Напишите класс для хранения информации о человеке: ФИО, возраст и т.п. на ваш выбор.
# У класса должны быть методы birthday для увеличения возраста на год, full_name для вывода полного ФИО и т.п. на ваш выбор.
# Убедитесь, что свойство возраст недоступно для прямого изменения, но есть возможность получить текущий возраст.

class Human:
    def __init__(self, fio, age):
        self.fio = fio
        self._age = age

    def birthday(self):
        self._age += 1

    def full_name(self):
        return f'{self.fio=}'

    def get_age(self):
        return self._age


if __name__ == '__main__':
    hunam = Human('Maria Lalala', 23)
    print(hunam.get_age())
    hunam.birthday()
    print(hunam.get_age())
    print(hunam.full_name())
