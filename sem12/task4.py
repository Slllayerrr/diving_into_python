# Доработайте класс прямоугольник из прошлых семинаров.
# Добавьте возможность изменять длину и ширину прямоугольника и встройте контроль недопустимых значений (отрицательных).
# Используйте декораторы свойств.

class Rectangle:
    def __init__(self, width, length=None):
        self._width = width
        if length:
            self._length = length
        else:
            self._length = width

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        if value > 0:
            self._width = value
        else:
            raise ValueError('Ширина должна быть больше 0!')

    @property
    def length(self):
        return self._length

    @length.setter
    def length(self, value):
        if value > 0:
            self._length = value
        else:
            raise ValueError('Длина должна быть больше 0!')

    def perimeter(self):
        return 2 * (self._width + self._length)

    def area(self):
        return self._length * self._width

    def __add__(self, other):
        # perim = self.perimeter() + other.perimeter()
        length = self._length + other.length
        width = self._width + other.width
        return Rectangle(width, length)

    def __sub__(self, other):
        # perim = abs(self.perimeter() - other.perimeter())
        length = abs(self._length - other.length)
        width = abs(self._width - other.width)
        return Rectangle(width, length)

    def __str__(self):
        return f'{self.length=}, {self.width=}, {self.perimeter()=}'


if __name__ == '__main__':
    rectangle_1 = Rectangle(3, 1)
    rectangle_2 = Rectangle(5, 2)
    rectangle_1.width = 5
    print(rectangle_1)

