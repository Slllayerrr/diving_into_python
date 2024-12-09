# Задание №4
# ✔ Создайте вручную список с повторяющимися элементами.
# ✔ Удалите из него все элементы, которые встречаются дважды
# 1, 5, 6, 4

# решение 1
new_list = [1, 5, 7, 0, 6, 4, 3, 2, 2, 4, 7, 7, 8, 6, 5, 2, 1, 19, 31, 21, 45]
TWO = 2

for item in new_list:
    if new_list.count(item) == 2:
        i = 0
        while TWO > i:
            new_list.remove(item)
            i += 1
print(new_list)

# решение 2
new_list = [1, 5, 7, 0, 6, 4, 3, 2, 2, 4, 7, 7, 8, 6, 5, 2, 1, 19, 31, 21, 45]

uniq_list = [item for item in new_list if new_list.count(item) != 2]
print(uniq_list)

# решение 3
new_list = [1, 5, 7, 0, 6, 4, 3, 2, 2, 4, 7, 7, 8, 6, 5, 2, 1, 19, 31, 21, 45]
uniq_list = []

for item in new_list:
    if new_list.count(item) != 2:
        uniq_list.append(item)
print(uniq_list)
