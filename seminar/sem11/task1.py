# Создайте класс Моя Строка, где: будут доступны все возможности str
# дополнительно хранятся имя автора строки и время создания (time.time)

class MyString(str):
    def __new__(cls, name, value):
        import time
        instance = super().__new__(cls, value)
        instance.name = name
        instance.time = time.time()
        print(f'Создан класс: {cls}, {name=}, {instance.time=}')
        return instance


if __name__ == '__main__':
    mystr = MyString('Mary', 'Hello wrld!')
