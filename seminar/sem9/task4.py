# Создайте декоратор с параметром.
# Параметр - целое число, количество запусков декорируемой функции.

from typing import Callable


# 1 вариант
#
# def deco_count(num: int):
#     def deco(func: Callable):
#         def wrapper(*args, **kwargs):
#             for cnt in range(1, num + 1):
#                 print(f'Функцию запустили {cnt} раз')
#                 res = func(*args, **kwargs)
#                 print(res)
#
#         return wrapper
#
#     return deco
#
#
# @deco_count(4)
# def summa(a: int, b: int):
#     return a + b


def deco_count(num: int):
    def deco(func: Callable):
        counter = []

        def wrapper(*args, **kwargs):
            for cnt in range(1, num + 1):
                print(f'Функцию запустили {cnt} раз')
                res = func(*args, **kwargs)
                counter.append(res)
            return counter

        return wrapper

    return deco


@deco_count(3)
def summa(a: int, b: int):
    return a + b


if __name__ == '__main__':
    print(summa(2, 3))
