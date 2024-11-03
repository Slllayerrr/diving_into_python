# ✔ Напишите функцию, которая принимает строку текста.
# ✔ Сформируйте список с уникальными кодами Unicode каждого символа введённой строки отсортированный по убыванию.


def fnk(text: str) -> list[int]:
    res = []
    for char in set(text):
        res.append(ord(char))
    return sorted(res, reverse=True)


text = input('Введите текст: ')
print(fnk(text))