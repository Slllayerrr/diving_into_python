# Задание №5
# ✔ Создайте вручную список с повторяющимися целыми числами.
# ✔ Сформируйте список с порядковыми номерами нечётных элементов исходного списка.
# ✔ Нумерация начинается с единицы.

# решение 1
new_list = [1, 1, 1, 1, 2, 2, 2, 7, 7, 7, 9, 9, 78, 78, 6, 5, 6, 5, 3, 3]
uniq_lst = []

for n, item in enumerate(new_list, 1):
    if item % 2:
        uniq_lst.append(n)
print(uniq_lst)

# решение 2
new_list = [1, 1, 1, 1, 2, 2, 2, 7, 7, 7, 9, 9, 78, 78, 6, 5, 6, 5, 3, 3]
uniq_lst = []
length = len(new_list)

uniq_lst = [n for n, elem in enumerate(new_list, 1) if elem % 2]
print(uniq_lst)

# решение 3
new_list = [1, 1, 1, 1, 2, 2, 2, 7, 7, 7, 9, 9, 78, 78, 6, 5, 6, 5, 3, 3]
uniq_lst = []
length = len(new_list)

uniq_lst = [i+1 for i in range(length) if new_list[i] % 2]
print(uniq_lst)
