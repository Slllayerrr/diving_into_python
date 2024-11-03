# ✔ Функция получает на вход строку из двух чисел через пробел.
# ✔ Сформируйте словарь, где ключом будет символ из Unicode, а значением — целое число.
# ✔ Диапазон пар ключ-значение от наименьшего из введённых пользователем чисел до наибольшего включительно.


def fnk(text: str) -> dict[str, int]:
    num1, num2 = map(int, text.split())
    res = {}
    for num in range(min(num1, num2), max(num1, num2) + 1):
        # res[chr(num)] = num       2 вариант
        res.setdefault(chr(num), num)
    return res


text = input('Введите два числа через пробел: ')
print(fnk(text))