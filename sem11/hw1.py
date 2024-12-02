# Добавьте ко всем задачам с семинара строки документации и методы вывода информации на печать. __str__ and __repr__
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
    def __str__(self):
        return f'Моя строка: {self.name}, "{self.time}"'

    def __repr__(self):
        return f'Архив: имя автора: {self.name}, время создания: "{self.time}"'

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

class Rectangle:
    """
        Класс прямоугольник. Класс принимает длину и ширину при создании экземпляра.
        У класса два метода, возвращающие периметр и площадь.
        Если при создании экземпляра передаётся только одна сторона, считаем что у нас квадрат.
    """
    def __init__(self, width, length=None):
        """Добавление параметров ширина и длина"""
        self.width = width
        if length:
            self.length = length
        else:
            self.length = width

    def perimeter(self):
        """Метод возвращает периметр"""
        return 2 * (self.width + self.length)

    def area(self):
        """Метод возвращает площадь"""
        return self.length * self.width

    def __add__(self, other):
        """Сложение и получение нового экземпляра класса"""
        # perim = self.perimeter() + other.perimeter()
        length = self.length + other.length
        width = self.width + other.width
        return Rectangle(width, length)

    def __sub__(self, other):
        # perim = abs(self.perimeter() - other.perimeter())
        length = abs(self.length - other.length)
        width = abs(self.width - other.width)
        return Rectangle(width, length)

    def __eq__(self, other):
        return self.area() == other.area()

    def __gt__(self, other):
        return self.area() > other.area()

    def __le__(self, other):
        return self.area() <= other.area()

    def __str__(self):
        return f'{self.length=}, {self.width=}, {self.perimeter()=}'

    def __repr__(self):
        return f'Прямоугольник: длина: {self.length}, ширина: {self.width}, периметр: {self.perimeter()}, плошадь: {self.area()}'



if __name__ == '__main__':
    rectangle_1 = Rectangle(3, 1)
    print(rectangle_1)
    print(repr(rectangle_1))

    archive = Archive(1, 'one')
    print(archive)
    print(repr(archive))

    mystr = MyString('Mary', 'Hello wrld!')
    print(mystr)
    print(repr(mystr))