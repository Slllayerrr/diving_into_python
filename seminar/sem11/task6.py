# Доработайте прошлую задачу.
# Добавьте сравнение прямоугольников по площади
# Должны работать все шесть операций сравнения
# __eq__ - равно, ==
# __ne__ - не равно, !=
# __gt__ - больше, >
# __ge__ - не больше, меньше или равно, <=
# __lt__ - меньше, <
# __le__ - не меньше, больше или равно, >

class Rectangle:
    def __init__(self, width, length=None):
        self.width = width
        if length:
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

    def __eq__(self, other):
        return self.area() == other.area()

    def __gt__(self, other):
        return self.area() > other.area()

    def __le__(self, other):
        return self.area() <= other.area()

    def __str__(self):
        return f'{self.length=}, {self.width=}, {self.perimeter()=}'


if __name__ == '__main__':
    rectangle_1 = Rectangle(3, 1)
    rectangle_2 = Rectangle(5, 2)

    print(rectangle_1.perimeter())
    print(rectangle_2.perimeter())
    print(rectangle_1.area())
    print(rectangle_2.area())
    print(rectangle_1 - rectangle_2)
    print(rectangle_1 + rectangle_2)
    print(rectangle_1 == rectangle_2)
    print(rectangle_1 != rectangle_2)
    print(rectangle_1 < rectangle_2)
    print(rectangle_1 > rectangle_2)
    print(rectangle_1 <= rectangle_2)
    print(rectangle_1 >= rectangle_2)

