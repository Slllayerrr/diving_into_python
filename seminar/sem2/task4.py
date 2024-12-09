# Задание №4
# ✔ Напишите программу, которая вычисляет площадь круга и длину окружности по введённому диаметру.
# ✔ Диаметр не превышает 1000 у.е.
# ✔ Точность вычислений должна составлять не менее 42 знаков после запятой.

import math
import decimal

PI = decimal.Decimal(math.pi)

decimal.getcontext().prec = 50

d = decimal.Decimal(input('Введите диаметр: '))
while d > 1000:
    print('Введено число вне диапазона')
    d = decimal.Decimal(input('Введите диаметр: '))
s = PI * (d/2)**2
l = PI * d
print(f'{s=} {l=}')
