# Создайте функцию аналог get для словаря.
# Помимо самого словаря функция принимает ключ и значение по умолчанию.
# При обращении к несуществующему ключу функция должна возвращать дефолтное значение.
# Реализуйте работу через обработку исключений.

# 1
# def my_get(my_dict, key, defolt_value=None):
#     try:
#         return my_dict[key]
#     except KeyError:
#         return defolt_value


# 2
def my_get(my_dict, key, defolt_value=None):
    res = defolt_value
    try:
        res = my_dict[key]
    except KeyError:
        pass
    return res




if __name__ == '__main__':
    test_dict = {1: 'hello', 2: 'wrld'}
    print(my_get(test_dict, 5, 'Такого значения нет'))