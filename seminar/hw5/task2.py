# Напишите однострочный генератор словаря, который принимает на вход три списка одинаковой длины:
# имена str, ставка int, премия str с указанием процентов вида «10.25%».
# В результате получаем словарь с именем в качестве ключа и суммой премии в качестве значения.
# Сумма рассчитывается как ставка умноженная на процент премии

names = ["Ivan", "Maria", "Filipp", "Irina"]
rates = [20_000, 30_000, 100_000, 40_00]
bonuses = ["10%", "25.5%", "13.3%", "42.73%"]

# 1 вариант
res_dict = {}
for name, rate, bonus in zip(names, rates, bonuses):
    res_dict[name] = rate* float(bonus.replace("%", ""))/100
print(res_dict)

# 2 вариант
res_dict_2 = {}
res = {name: rate* float(bonus.replace("%", ""))/100 for name, rate, bonus in zip(names, rates, bonuses)}
print(res)