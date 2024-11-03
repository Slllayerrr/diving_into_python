# Напишите функцию, принимающую на вход только ключевые
# параметры и возвращающую словарь, где ключ — значение
# переданного аргумента, а значение — имя аргумента. Если
# ключ не хешируем, используйте его строковое представление.
#
def key_params(*, a, b, c, d) -> dict:
    dict_hash = {}
    dict_vars = locals()
    lst = [a, b, c, d]
    for i in lst:
        for key, values in dict_vars.items():
            if values == i:
                if type(i) == list or type(i) == set or type(i) == dict:
                    dict_hash[str(i)] = key
                else:
                    dict_hash[i] = key
    return dict_hash


print(key_params(a=1, b='hello', c=[1,2,3], d={}))
