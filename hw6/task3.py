# Напишите функцию в шахматный модуль.
# Используйте генератор случайных чисел для случайной расстановки ферзей в задаче выше.
# Проверяйте различный случайные варианты и выведите 4 успешных расстановки.

from itertools import combinations
from random import randint


def rnd_ferz():
    queen = []
    for _ in range(8):
        num = (randint(1, 8)), (randint(1, 8))
        queen.append(num)
    return queen


def is_attacking(q1, q2):
    return q1[0] == q2[0] or q1[1] == q2[1] or abs(q1[0] - q2[0]) == abs(q1[1] - q2[1])


def check_queens():
    for q1, q2 in combinations(rnd_ferz(), 2):
        if is_attacking(q1, q2):
            return False
    return True


print(check_queens())
