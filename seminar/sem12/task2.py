# Доработаем задачу 1.
# Создайте менеджер контекста, который при выходе сохраняет значения в JSON файл.

from collections import deque
import json
import time


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

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        dump_dict = {}
        while self._memory:
            dump_dict.update(self._memory.popleft())
            print(dump_dict)
        with open(f'{int(time.time())}.json', 'w', encoding='utf-8') as f:
            json.dump(dump_dict, f)

if __name__ == '__main__':
    fact = Factorial(7)
    for i in range(15):
        print(fact(i))
        print(fact.print_memory())
    with fact as fd:
        fd(3)