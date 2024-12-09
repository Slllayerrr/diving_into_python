# На семинарах по ООП был создан класс прямоугольник хранящий длину и ширину,
# а также вычисляющую периметр, площадь и позволяющий складывать и вычитать прямоугольники беря за основу периметр.
# Напишите 3-7 тестов unittest для данного класса.
import unittest


class TestRectangle(unittest.TestCase):
    def setUp(self):
        self.r1 = Rectangle(1, 1)
        self.r2 = Rectangle(10, 20)
        self.r3 = Rectangle(2, 5)
        self.r4 = Rectangle(20, 10)

    def test_create(self):
        self.assertEqual(Rectangle(1, 1), self.r1)

    def test_perimetr(self):
        self.assertEqual(self.r2.perimeter(), 60)

    def test_area(self):
        self.assertEqual(self.r3.area(), 10)

    def test_perimetr_equal(self):
        self.assertEqual(self.r4.perimeter(), self.r2.perimeter())

    def test_area_non_equal(self):
        self.assertNotEqual(self.r4.area(), self.r1.area())

    def test_add(self):
        self.assertEqual(self.r2 + self.r4, Rectangle(30, 30))

    def test_sub(self):
        self.assertEqual(self.r3 - self.r1, Rectangle(1, 4))


class Rectangle:
    __slots__ = ['_width', '_length']

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

    def __eq__(self, other):
        return self.area() == other.area()

    def __str__(self):
        return f'{self.length=}, {self.width=}, {self.perimeter()=}'


if __name__ == '__main__':
    unittest.main(verbosity=2)
