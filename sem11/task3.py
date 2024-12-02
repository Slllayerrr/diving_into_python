# Добавьте к задачам 1 и 2 строки документации для классов.

class MyString(str):
    """
    Класс Моя Строка, где: будут доступны все возможности str
    дополнительно хранятся имя автора строки и время создания
    """
    def __new__(cls, name, value):
        import time
        instance = super().__new__(cls, value)
        instance.name = name
        instance.time = time.time()
        print(f'Создан класс: {cls}, {name=}, {instance.time=}')
        return instance

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

if __name__ == '__main__':
    help(Archive)
