# Напишите функцию, которая принимает на вход строку — абсолютный путь до файла.
# Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.


def tuple_file(inp_str):
    *a, b, c = inp_str.split('/')
    name_file, file_extension = c.split('.')
    res = (inp_str, name_file, file_extension)
    return res


inp_str = 'D:DataMyFilesile.png'
print(tuple_file(inp_str))
