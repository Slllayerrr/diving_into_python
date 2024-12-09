# ✔ Функция получает на вход список чисел.
# ✔ Отсортируйте его элементы in place без использования встроенных в язык сортировок.
# ✔ Как вариант напишите сортировку пузырьком. Её описание есть в википедии.


def fnk(lst: list) -> list:
    for i in range(len(lst)):
        swapped = True
        for j in range(0, len(lst)-i-1):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j + 1], lst[j]
                swapped= False
        if swapped:
            return lst


lst_num = [23, 54, 45, 232, 64]
print(fnk(lst_num))
