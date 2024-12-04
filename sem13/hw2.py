# Допишите в вашу задачу Archive обработку исключений.
# Добавьте исключение в ваш код InvalidTextError, которые будет вызываться, когда текст не является строкой или является пустой строкой.
# Текст ошибки: Invalid text: (введенный текст). Text should be a non-empty string:
# И InvalidNumberError, которое будет вызываться, если число не является положительным целым числом или числом с плавающей запятой.
# Текст ошибки: 'Invalid number: (введенное число}. Number should be a positive integer or float.'
class InvalidTextError(Exception):
    def __init__(self, text):
        super().__init__(f'Invalid text: {text}. Text should be a non-empty string.')


class InvalidNumberError(Exception):
    def __init__(self, number):
        super().__init__(f'Invalid number: {number}. Number should be a positive integer or float.')


class Archive:
    _instance = None

    def __init__(self, num, text):
        if not isinstance(text, str) or not text.strip():
            raise InvalidTextError(text)
        if not (isinstance(num, (int, float)) and num > 0):
            raise InvalidNumberError(num)

        self.num = num
        self.text = text

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)

            # Инициализация списков для хранения архива
            cls._instance.list_num = []
            cls._instance.list_text = []

        else:
            cls._instance.list_num.append(cls._instance.num)
            cls._instance.list_text.append(cls._instance.text)

        return cls._instance

    def __str__(self):
        return f'Архив: {self.num}, "{self.text}"'

    def __repr__(self):
        return (f'Архив: номер: {self.num}, текст: "{self.text}", '
                f'а также списки: {self.list_num} и {self.list_text}')

if __name__ == '__main__':
    archive = Archive(num=-5, text='one')
    archive2 = Archive(2, 'two')
    archive3 = Archive(3, 'three')
    print(archive)
    print(repr(archive))