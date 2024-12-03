# Создайте три (или более) отдельных классов животных. Например рыбы, птицы и т.п.
# У каждого класса должны быть как общие свойства, например имя, так и специфичные для класса.
# Для каждого класса создайте метод, выводящий информацию специфичную для данного класса.

class Fish:
    def __init__(self, name, weight, max_depth, color):
        self.name = name
        self.weight = weight
        self.max_depth = max_depth
        self.color = color

    def get_depth(self):
        if self.max_depth < 10:
            return 'Мелководная'
        elif self.max_depth > 100:
            return 'Глубоководная'
        else:
            return 'Средневодная'


class Bird:
    def __init__(self, name, weight, wingspan, color):
        self.name = name
        self.weight = weight
        self.wingspan = wingspan
        self.color = color

    def get_wing_length(self):
        return self.wingspan / 2


class Mammal:
    def __init__(self, name, weight, height, color):
        self.name = name
        self.weight = weight
        self.height = height
        self.color = color

    def get_category(self):
        if self.height < 10:
            return 'Карликовый'
        elif self.height > 80:
            return 'Гигантский'
        else:
            return 'Средний'


if __name__ == '__main__':
    clown = Fish('Немо', 1, 20, 'Оранжевый')
    penguin = Bird('Ковальски', 20, 60, 'Черный')
    zebra = Mammal('Мартин', 150, 120, 'Белый')
    print(penguin.get_wing_length())
    print(clown.get_depth())
    print(zebra.get_category())