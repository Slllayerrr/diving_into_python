# Задание №2
# Пользователь вводит данные.
# Сделайте проверку данных и преобразуйте если возможно в один из вариантов ниже:
# ✔ Целое положительное число
# ✔ Вещественное положительное или отрицательное число
# ✔ Строку в нижнем регистре, если в строке есть хотя бы одна заглавная буква
# ✔ Строку в верхнем регистре в остальных случаях

# 3.14  -3.14  .342   3452.

data = input('Введите данные: ')

if data.isdigit():  # является ли строка числом
    res = int(data)
elif data.replace('.', '').replace('-', '').isdigit() \
        and data.count('.') < 2 and '-' not in data[1:]:
    res = float(data)
elif data != data.lower():  # not data.islower
    res = data.lower()
else:
    res = data.upper()

print(res)
