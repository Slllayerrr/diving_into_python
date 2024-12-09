# Доработаем класс Архив из задачи 2.
# Добавьте методы представления экземпляра для программиста и для пользователя.

class Archive:
    """
    Класс Архив, который хранит пару свойств. При создании нового экземпляра класса,
    старые данные из ранее созданных экземпляров сохраняются в пару списков архивов
    """
    _instance = None

    def __init__(self, num, text):
        self.num = num
        self.text = text

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
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
    archive = Archive(1, 'one')
    archive2 = Archive(2, 'two')
    archive3 = Archive(3, 'three')
    print(archive)
    print(repr(archive))
