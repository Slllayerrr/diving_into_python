# ✔ Напишите программу, которая выводит на экран числа от 1 до 100.
# ✔ При этом вместо чисел, кратных трем, программа должна выводить слово «Fizz»
# ✔ Вместо чисел, кратных пяти — слово «Buzz».
# ✔ Если число кратно и 3, и 5, то программа должна выводить слово «FizzBuzz».
# ✔ *Превратите решение в генераторное выражение.

LOW_LIMIT = 1
UP_LIMIT = 101
DIV_1 = 3
DIV_2 = 5

# 1 вариант
res = []
for item in range(1, 100 + 1):
    if item % (DIV_1 * DIV_2) == 0:
        res.append('FizzBuzz')
        print('FizzBuzz')
    elif item % DIV_1 == 0:
        print('Fizz')
        res.append('Fizz')
    elif item % DIV_2 == 0:
        print('Buzz')
        res.append('Buzz')
    else:
        print(item)
        res.append(item)
print(res)

# 2 вариант
res_2 = (
    'FizzBuzz' if item % (DIV_1 * DIV_2) == 0 else
    'Fizz' if item % DIV_1 == 0 else
    'Buzz' if item % DIV_2 == 0 else item
    for item in range(1, 100 + 1)
)
print(*res_2)
