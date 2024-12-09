# Задание №7
# ✔ Пользователь вводит строку текста.
# ✔ Подсчитайте сколько раз встречается
# каждая буква в строке без использования метода count и с ним.
# ✔ Результат сохраните в словаре, где ключ —
# символ, а значение — частота встречи символа в строке.
# ✔ Обратите внимание на порядок ключей.
# Объясните почему они совпадают или не совпадают в ваших решениях.

# решение 1
text = input('Введите строку текста: ')
res_dict = {}
for item in set(text):
    res_dict[item] = text.count(item)
print(res_dict)


# решение 2
res_dict = {}
for char in text:
    if char not in res_dict:
        res_dict[char] = 1
    else:
        res_dict[char] += 1
print(res_dict)


# решение 3
res_dict = {}
for char in text:
    res_dict[char] = res_dict.get(char, 0)+1
print(res_dict)