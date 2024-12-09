import unittest


class TestAnimal(unittest.TestCase):
    def setUp(self):
        self.f1 = Fish('Немо', 1, 2, 'Оранжевый')
        self.f2 = Fish('Немо', 1, 200, 'Оранжевый')
        self.f3 = Fish('Немо', 1, 20, 'Оранжевый')
        self.b1 = Bird('Ковальски', 20, 60, 'Черный')
        self.m1 = Mammal('Мартин', 150, 8, 'Белый')
        self.m2 = Mammal('Мартин', 150, 120, 'Белый')
        self.m3 = Mammal('Мартин', 150, 80, 'Белый')

    def test_shallow_fish(self):
        self.assertEqual('Мелководная', self.f1.get_depth())

    def test_deep_fish(self):
        self.assertEqual('Глубоководная', self.f2.get_depth())

    def test_medium_fish(self):
        self.assertEqual('Средневодная', self.f3.get_depth())

    def test_bird_wing(self):
        self.assertEqual(self.b1.get_wing_length(), 30)

    def test_mammal_dwarf(self):
        self.assertEqual(self.m1.get_category(), 'Карликовый')

    def test_mammal_gigantic(self):
        self.assertEqual(self.m2.get_category(), 'Гигантский')

    def test_mammal_medium(self):
        self.assertEqual(self.m3.get_category(), 'Средний')




class Animal:
    def __init__(self, name, weight,  color):
        self.name = name
        self.weight = weight
        self.color = color

class Fish(Animal):
    def __init__(self, name, weight, max_depth, color):
        super().__init__(name, weight, color)
        self.max_depth = max_depth


    def get_depth(self):
        if self.max_depth < 10:
            return 'Мелководная'
        elif self.max_depth > 100:
            return 'Глубоководная'
        else:
            return 'Средневодная'


class Bird(Animal):
    def __init__(self, name, weight, wingspan, color):
        super().__init__(name, weight, color)
        self.wingspan = wingspan


    def get_wing_length(self):
        return self.wingspan / 2


class Mammal(Animal):
    def __init__(self, name, weight, height, color):
        super().__init__(name, weight, color)
        self.height = height

    def get_category(self):
        if self.height < 10:
            return 'Карликовый'
        elif self.height > 80:
            return 'Гигантский'
        else:
            return 'Средний'

if __name__ == '__main__':
    unittest.main(verbosity=2)