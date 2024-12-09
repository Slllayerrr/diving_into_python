# Создайте функцию-замыкание, которая запрашивает два целых числа:
# ○ от 1 до 100 для загадывания,
# ○ от 1 до 10 для количества попыток
# Функция возвращает функцию, которая через консоль просит угадать загаданное число за указанное число попыток.


def guess_num(num: int, cnt: int):
    def guess_name():
        for i in range(1, cnt + 1):
            print(f'Попытка: {i}')
            user_input = int(input('Введите число от 1 до 100: '))
            if num == user_input:
                print(f'Число отгадано с {i} попытки')
                return
            elif num > user_input:
                print('Ваше число меньше загаданного')
            elif num < user_input:
                print('Ваше число больше загаданного')

    return guess_name


if __name__ == '__main__':
    game = guess_num(50, 10)
    game()