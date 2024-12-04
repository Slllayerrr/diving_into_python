# Создайте функцию, которая запрашивает числовые данные от
# пользователя до тех пор, пока он не введёт целое или вещественное число.
# Обрабатывайте не числовые данные как исключения.

def get_num()-> int | float:
    while True:
        num = input('Введите число: ')
        try:
            n = float(num)
            break
        except ValueError:
            print('Вы ввели не число!')
    try:
        n = int(num)
    except ValueError:
        pass
    return n

if __name__ == '__main__':
    print(get_num())
