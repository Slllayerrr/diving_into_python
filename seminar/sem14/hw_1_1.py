# ✔ Напишите программу, которая решает квадратные уравнения даже если дискриминант отрицательный.
# ✔ Используйте комплексные числа для извлечения квадратного корня.
# 2-5 тестов на задачу в трёх вариантах:
# ○ doctest
import doctest

def discriminant(a, b, c):
    """
    >>> discriminant(-1,7,8)
    '-1.0, 8.0'

    >>> discriminant(4, 4, 1)
    '-0.5'

    >>> discriminant(2,1,1)
    '(-0.24999999999999997+0.6614378277661477j), (-0.25000000000000006-0.6614378277661477j)'

    """

    d = b ** 2 - 4 * a * c
    if d > 0:
        x1 = (-b + d ** 0.5) / (2 * a)
        x2 = (-b - d ** 0.5) / (2 * a)
        res = f'{x1}, {x2}'
    elif d == 0:
        x = -b / (2 * a)
        res = f'{x}'
    else:
        x1 = (-b + d ** 0.5) / (2 * a)
        x2 = (-b - d ** 0.5) / (2 * a)
        res = f'{x1}, {x2}'

    return res


if __name__ == '__main__':


    doctest.testmod(verbose=True)
