# Создайте класс-функцию, который считает факториал числа при вызове экземпляра.
# Экземпляр должен запоминать последние k значений.
# Параметр k передаётся при создании экземпляра.
# Добавьте метод для просмотра ранее вызываемых значений и их факториалов.

from collections import deque


class Factorial:
    def __init__(self, k):
        self._memory = deque(maxlen=k)

    def __call__(self, n, *args, **kwargs):
        res = 1
        for num in range(2, n + 1):
            res += num
        self._memory.append({n: res})
        return self._memory[-1]

    def print_memory(self):
        return self._memory


if __name__ == '__main__':
    f = Factorial(3)
    for i in range(15):
        print(f(i))
        print(f.print_memory())


