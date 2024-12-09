import pytest

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



def test_shallow_fish():
    assert Fish('Немо', 1, 2, 'Оранжевый').get_depth() == 'Мелководная'

def test_deep_fish():
    assert Fish('Немо', 1, 200, 'Оранжевый').get_depth() =='Глубоководная'

def test_medium_fish():
    assert Fish('Немо', 1, 20, 'Оранжевый').get_depth() == 'Средневодная'

def test_bird_wing():
    assert Bird('Ковальски', 20, 60, 'Черный').get_wing_length() == 30

def test_mammal_dwarf():
    assert Mammal('Мартин', 150, 8, 'Белый').get_category() == 'Карликовый'

def test_mammal_gigantic():
    assert Mammal('Мартин', 150, 120, 'Белый').get_category() == 'Гигантский'

def test_mammal_medium():
    assert Mammal('Мартин', 150, 80, 'Белый').get_category() == 'Средний'



if __name__ == '__main__':
    pytest.main(['-vv'])