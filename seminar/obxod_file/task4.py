# ✔ Создайте генератор чётных чисел от нуля до 100.
# ✔ Из последовательности исключите числа, сумма цифр которых равна 8.
# ✔ Решение в одну строку.
limit = 100

# 1 вариант
list_ = []
for number in range(0, limit + 1, 2):
    if number % 10 + number // 10 != 8:
        list_.append(number)
print(list_)

# 2 вариант
even_num = (number for number in range(0, 100 + 1, 2) if number % 10 + number // 10 != 8)
print(*even_num)
