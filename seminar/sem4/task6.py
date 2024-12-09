# ✔ Функция получает на вход список чисел и два индекса.
# ✔ Вернуть сумму чисел между переданными индексами.
# ✔ Если индекс выходит за пределы списка, сумма считается до конца и/или начала списка.

def sum_lst(numbers: list[int | float], num1: int, num2: int) -> int | float:
    size = len(numbers)
    min_i, max_i = sorted([num1, num2])
    min_i = min_i if min_i > 0 else 0
    max_i = max_i if max_i < size else size
    return sum(numbers[min_i: max_i])


number = [11, 45, 33, 65, 4, 7, 3]
print(sum_lst(number, -8,1))