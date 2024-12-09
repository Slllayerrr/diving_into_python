# Создайте класс прямоугольник.
# Класс должен принимать длину и ширину при создании экземпляра.
# У класса должно быть два метода, возвращающие периметр и площадь.
# Если при создании экземпляра передаётся только одна сторона, считаем что у нас квадрат.

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


if __name__ == '__main__':
    rectangle_1 = Rectangle(3)
    print(rectangle_1.perimeter())
    print(rectangle_1.area())
