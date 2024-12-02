# Создайте класс Архив, который хранит пару свойств. Например, число и строку.
# При создании нового экземпляра класса, старые данные из ранее созданных экземпляров сохраняются в пару списков архивов
# list-архивы также являются свойствами экземпляра

class Archive:
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
    archive = Archive(1, 'one')
    archive2 = Archive(2, 'two')
    archive3 = Archive(3, 'three')
    print(f'{archive.list_text}')
