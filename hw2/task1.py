# Напишите программу, которая получает целое число и возвращает его шестнадцатеричное
# строковое представление. Функцию hex используйте для проверки своего результата

HEX = 16
A = 10
B = 11
C = 12
D = 13
E = 14
F = 15

num = int(input(f'Введите целое число: '))
test_num = num
res = ''

while test_num:
    cur_num = test_num % HEX
    if cur_num in (A, B, C, D, E, F):
        if cur_num == A:
            res = 'A' + res
        elif cur_num == B:
            res = 'B' + res
        elif cur_num == C:
            res = 'C' + res
        elif cur_num == D:
            res = 'D' + res
        elif cur_num == E:
            res = 'E' + res
        else:
            res = 'F' + res
    else:
        res = str(cur_num) + res
    test_num //= HEX
print(res)
print(hex(num))
