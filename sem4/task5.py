# ✔ Функция принимает на вход три списка одинаковой длины:
# ✔ имена str,
# ✔ ставка int,
# ✔ премия str с указанием процентов вида «10.25%».
# ✔ Вернуть словарь с именем в качестве ключа и суммой премии в качестве значения.
# ✔ Сумма рассчитывается как ставка умноженная на процент премии.
import decimal


def dict_bonus(names: list[str], salaries: list[str], bonuses: list[str]) -> dict[str: decimal.Decimal]:
    res = {}
    for name, salary, bonus in zip(names, salaries, bonuses):
        res[name] = salary * decimal.Decimal(bonus[:-1]) #decimal.Decimal(bonus.replace("%", "")) - 2 вариант
    return res


n = ["Иван", "Николай", "Пётр", "Харитон"]
s = [125_000, 96_000, 109_000, 100_000]
a = ["10%", "25.5%", "13.3%", "42.73%"]
print(dict_bonus(n, s, a))
