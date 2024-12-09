# � Добавьте в модуль с загадками функцию, которая принимает на вход строку (текст загадки) и число (номер попытки, с которой она угадана).
# � Функция формирует словарь с информацией о результатах отгадывания.
# � Для хранения используйте защищённый словарь уровня модуля.
# � Отдельно напишите функцию, которая выводит результаты угадывания из защищённого словаря в удобном для чтения виде.
# � Для формирования результатов используйте генераторное выражение.

__all__ = ['save', 'show', 'secters', 'storage']

_data = {}


def save(pazle: str, count: int) -> None:
    _data.update({pazle: count})


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
        save(key, res)
        print(_data)


def show():
    res = (
        f'Загадку {pazzle} гадал с {count}-й попытки' if count
        else f'Загадку {pazzle} не угадал'
        for pazzle, count in _data.items()
    )
    print(*res, sep='\n')


if __name__ == '__main__':
    storage()
    print()
    show()
