# Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения.
# Определите какие вещи влезут в рюкзак передав его максимальную грузоподъёмность.
# Достаточно вернуть один допустимый вариант.


MAX_WEGHT = 1.0

items = {
    "ключи": 0.3,
    "кошелек": 0.2,
    "телефон": 0.5,
    "зажигалка": 0.1,
}
sum = 0
unique = {}

for first_thing, first_weght in items.items():
    if first_thing not in unique:
        if sum + first_weght <= MAX_WEGHT:
            unique[first_thing] = first_weght
            sum += first_weght
        else:
            print(f'Масса вещей в рюкзаке: {sum} , вещи, которые влезли в рюкзак: {unique}')