# Напишите код, который запрашивает число и сообщает, является ли оно простым или составным.
# Используйте правило для проверки: «Число является простым, если делится нацело только на единицу
# и на себя». Сделайте ограничение на ввод отрицательных чисел и чисел больше 100 тысяч.

MIN_LIMIT = 3
MAX_LIMIT = 100_000
START = 2
num = int(input(f'Введите число от 2 до 100000:'))

if num > MIN_LIMIT and num < MAX_LIMIT:
    while START < num - 1:
        if num % START == 0:
            res = 'Число является составным'
            START += 1
        else:
            res = 'Число является простым'
            START += 1
elif num == 2:
    res = 'Число является простым'
else:
    res = 'неправильно введено число!'
print(res)