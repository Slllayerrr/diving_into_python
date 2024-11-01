# Задание №1
# ✔ Вручную создайте список с целыми числами, которые повторяются.
# Получите новый список, который содержит уникальные (без повтора) элементы исходного списка.
# ✔ Подготовьте два решения, короткое и длинное, которое не использует другие коллекции помимо списков.

list1 = [1, 2, 3, 4, 4, 5, 3, 4, 2, 7, 8]

# решение 1
sort_lst = list(set(list1))
print(sort_lst)

# решение 2
sort_lst2 = []
list1.sort()
i = 0
while i < len(list1):
    spam = sort_lst2.count(list1[i])
    if spam == 0:
        sort_lst2.append(list1[i])
    i += 1
print(sort_lst2)

# решение 3
sort_lst3 = []
for item in list1:
    if item not in sort_lst3:
        sort_lst3.append(item)
print(sort_lst3)

# решение 4
new_list = sorted(list1)
for i in range(len(new_list) - 1, 0, -1):
    if new_list[i] == new_list[i - 1]:
        del new_list[i]  # del - удаление объекта
print(new_list)
