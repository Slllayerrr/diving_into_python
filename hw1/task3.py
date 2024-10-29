# Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток. Программа
# должна подсказывать «больше» или «меньше» после каждой попытки. Для генерации случайного
# числа используйте код:

from random import randint

LOWER_LIMIT = 0
UPPER_LIMIT = 1000
ATTEMPT = 10
i = 1
num = randint(LOWER_LIMIT, UPPER_LIMIT)

while i <= ATTEMPT:
    print(f'попытка №{i}')
    num_new = int(input('Число: '))
    if num > num_new:
        print('больше')
        i += 1
    elif num < num_new:
        print('меньше')
        i += 1
    else:
        print(f'{num} - загаданное число')
        break