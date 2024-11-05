# ✔ Продолжаем развивать задачу 2.
# ✔ Возьмите словарь, который вы получили. Сохраните его итераторатор.
# ✔ Далее выведите первые 5 пар ключ-значение, обращаясь к итератору, а не к словарю

#  задача 2 :
str_1 = 'оздайте из строки словар'
res = {char: ord(char) for char in str_1}
print(res)
#
COUNT = 5
dict_res = iter(res.items())
print(dict_res)

for _ in range(COUNT):
    print(next(dict_res))
    # print(*next(dict_res))
