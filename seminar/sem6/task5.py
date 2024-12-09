# � Добавьте в модуль с загадками функцию, которая хранит словарь списков.
# � Ключ словаря - загадка, значение - список с отгадками.
# � Функция в цикле вызывает загадывающую функцию, чтобы передать ей все свои загадки.

def secters(pazzle: str, answers: list[str], count: int = 3) -> int:
    print(f'Отгадайте загадку: {pazzle}')
    for i in range(1, count + 1):
        answer = input(f'Попытка номер {i}. Ответ: ').lower()
        if answer in answers:
            return i
    return 0


def storage():
    puzzles = {
        'Зимой и летом одним цветом': ['ёлка', 'ель', 'доллар', 'сосна'],
        'Висит груша - нельзя скушать': ['лампа', 'лампочка', 'люстра'],
        'Сидит дед - во сто шуб одет': ['лук', 'луковица', 'капуста']
    }
    # print(puzzles.items())
    for key, value in puzzles.items():
        res = secters(key, value)
        print(f'Угадал с {res} попытки' if res else f'Не угадал')


if __name__ == '__main__':
    storage()
