# Добавьте в задачу Rectangle, которую писали ранее, исключение NegativeValueError,
# которое выбрасывается при некорректных значениях ширины и высоты


class NegativeValueError(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f'Параметр должен быть больше нуля! Ваш параметр {self.value}.'


class Range:

    def __set_name__(self, owner, name):
        self.param_name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.param_name)

    def __set__(self, instance, value):
        self.validate(value)
        setattr(instance, self.param_name, value)

    def validate(self, value):
        if value < 1:
            raise NegativeValueError(value)


class Rectangle:
    width = Range()
    length = Range()

    def __init__(self, width, length=None):
        self.width = width
        if length is not None:
            self.length = length
        else:
            self.length = width

    def perimeter(self):
        return 2 * (self.width + self.length)

    def area(self):
        return self.length * self.width

    def __add__(self, other):
        # perim = self.perimeter() + other.perimeter()
        length = self.length + other.length
        width = self.width + other.width
        return Rectangle(width, length)

    def __sub__(self, other):
        # perim = abs(self.perimeter() - other.perimeter())
        length = abs(self.length - other.length)
        width = abs(self.width - other.width)
        return Rectangle(width, length)

    def __str__(self):
        return f'{self.length=}, {self.width=}, {self.perimeter()=}'


if __name__ == '__main__':
    rectangle_1 = Rectangle(3, -2)
    rectangle_2 = Rectangle(5, 2)
    print(rectangle_1)
