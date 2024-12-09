# Задание №3
# ✔ Создайте вручную кортеж содержащий элементы разных типов.
# ✔ Получите из него словарь списков, где:
# ключ — тип элемента,
# значение — список элементов данного типа.

# решение 1
new_tuple = (23, 234.40, 'dfvsxx', [3, 2, 2])
res_dict = {}
for item in new_tuple:
    item_type = type(item)
    if item_type not in res_dict:
        res_dict[item_type] = [item]
    else:
        res_dict[item_type].append(item)
print(res_dict)

# решение 2
new_tuple = (23, 234.40, 'dfvsxx', [3, 2, 2])
res_dict = {}
for item in new_tuple:
    item_type = type(item)
    if item_type not in res_dict:
        res_dict[item_type] = [el for el in new_tuple if type(el) == item_type]
print(res_dict)

# решение 3
new_tuple = (23, 234.40, 'dfvsxx', [3, 2, 2])
res_dict = {}
for item in new_tuple:
    key = res_dict.setdefault(type(item), [])
    key.append(item)
print(res_dict)
