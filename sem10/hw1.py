# Доработаем задачи 5-6. Создайте класс-фабрику.
# ○ Класс принимает тип животного (название одного из созданных классов) и параметры для этого типа.
# ○ Внутри класса создайте экземпляр на основе переданного типа и верните его из класса-фабрики.


class Animal:
    def __init__(self, name, weight, color):
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


class AnimalFactory:

    def create_animal(self, animal_type, *args):
        if animal_type == 'Fish':
            return Fish(*args)
        elif animal_type == 'Bird':
            return Bird(*args)
        elif animal_type == 'Mammal':
            return Mammal(*args)
        else:
            return 'Неверный тип животного!'


if __name__ == '__main__':
    factory = AnimalFactory()
    animal1 = factory.create_animal('Bird', 'Ковальски', 20, 60, 'Черный')
    animal2 = AnimalFactory().create_animal('Fish', 'Немо', 1, 20, 'Оранжевый')
    animal3 = AnimalFactory().create_animal('Mammal', 'Мартин', 150, 120, 'Белый')
    print(f'{animal2.get_depth()=}')
    print(f'{animal1.get_wing_length()=}')
    print(f'{animal3.get_category()=}')
