# исключения InvalidNameError и InvalidAgeError, если данные неверные.
# Исключение Invalidld Error, если ID неверный.

# Создайте класс Сотрудник.
# Воспользуйтесь классом человека из прошлого задания.
# У сотрудника должен быть:
# ○ шестизначный идентификационный номер
# ○ уровень доступа вычисляемый как остаток от деления суммы цифр id на семь

class InvalidNameError(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f'Имя не должно быть пустым! Ваше имя: "{self.value}".'


class InvalidAgeError(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f'Возраст должен быть целым положительным числом! Ваш возраст: {self.value}.'


class InvalidIdError(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f'Id должен быть шестизначным положительным целым числом! Ваш id: {self.value}.'


class Human:
    def __init__(self, fio, age):
        if len(fio) == 0:
            raise InvalidNameError(fio)
        self.fio = fio
        if not (isinstance(age, (int)) and age > 0):
            raise InvalidAgeError(age)
        self._age = age

    def birthday(self):
        self._age += 1

    def full_name(self):
        return f'{self.fio=}'

    def get_age(self):
        return self._age


class Worker(Human):
    MAX_LEVEL = 7
    MIN_ID = 100_000
    MAX_ID = 999_999

    def __init__(self, user_id, fio, age):
        super().__init__(fio, age)

        if user_id < self.MIN_ID or user_id > self.MAX_ID or user_id < 0:
            raise InvalidIdError(user_id)
        self.user_id = user_id

    def access(self):
        user_id_str = str(self.user_id)
        summa = sum(int(num) for num in user_id_str)
        return summa % self.MAX_LEVEL


if __name__ == '__main__':
    worker = Worker(1545, 'Lola', 43)
    print(worker.user_id, worker.access())
