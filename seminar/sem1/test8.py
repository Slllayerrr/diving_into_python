# Задание №8
# Нарисовать в консоли ёлку спросив
# у пользователя количество рядов.
# Пример результата:
# Сколько рядов у ёлки? 5
#     *
#    ***
#   *****
#  *******
# *********

SPACE = ' '
STAR = '*'

rows = int(input('Сколько рядов у ёлки? '))
spaces = rows - 1
stars = 1

for _ in range(rows):
    print((spaces * SPACE) + (stars * STAR))
    stars += 2
    spaces -= 1
