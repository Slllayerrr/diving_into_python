# Задание №6
# Напишите программу банкомат.
# ✔ Начальная сумма равна нулю
# ✔ Допустимые действия: пополнить, снять, выйти
# ✔ Сумма пополнения и снятия кратны 50 у.е.
# ✔ Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
# ✔ После каждой третей операции пополнения или снятия начисляются проценты - 3%
# ✔ Нельзя снять больше, чем на счёте
# ✔ При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой операцией, даже ошибочной
# ✔ Любое действие выводит сумму денег

import decimal

CMD_DEPOSIT = 'п'
CMD_WITHDRAW = 'с'
CMD_EXIT = 'в'
NUMBER_OPERATION = 3
MULTIPLISITY = 50
PRECENT_WITHDRAWAL = decimal.Decimal(15 / decimal.Decimal(1000))
PRECENT_RICHNESS = decimal.Decimal(10 / decimal.Decimal(100))
RICHNESS_SUM = decimal.Decimal(5_000_000)
MIN_REMOVAL = decimal.Decimal(30)
MAX_REMOVAL = decimal.Decimal(600)
PRECENT_BONUS = decimal.Decimal(3) / decimal.Decimal(100)

balance = decimal.Decimal(0)
count = 0

while True:
    action = input(f'Пополнить - "{CMD_DEPOSIT}", Снять - "{CMD_WITHDRAW}", Выйти - "{CMD_EXIT}",')
    if action == CMD_EXIT:
        print(f'Заберите карту. Баланс: {balance}у.е')
        break
    if balance > RICHNESS_SUM:
        present = balance * PRECENT_RICHNESS
        balance -= present
        print(f'Вычтен налог на богатство {PRECENT_RICHNESS * 100}%.'
              f'Сумма процента - {present}. Баланс карты - {balance}у.е.')
    if action in (CMD_DEPOSIT, CMD_WITHDRAW):
        amount = 1
        while amount % MULTIPLISITY != 0:
            amount = decimal.Decimal(input(f'Введите сумму кратную {MULTIPLISITY}: '))
        if action == CMD_DEPOSIT:
            balance += amount
            count += 1
            print(f'Зачислено {amount}у.е. Баланс карты - {balance}у.е.')
        elif action == CMD_WITHDRAW:
            precent = amount * PRECENT_WITHDRAWAL
            precent = MIN_REMOVAL if precent < MIN_REMOVAL else MAX_REMOVAL if precent > MAX_REMOVAL else precent
            sub = amount + precent
            if balance > sub:
                balance -= sub
                count += 1
                print(f'Снятие с карты {amount}у.е. Сумма процента за снятие {precent}. Баланс карты {balance}.')
            else:
                print(f'Недостаточно средств. Сумма снятия {amount}у.е. Сумма процента за снятие {precent}. Баланс карты {balance}.')
    if count % NUMBER_OPERATION == 0:
        bonus = balance * PRECENT_BONUS
        balance += bonus
        print(f'Начислен бонус {bonus} за каждую {NUMBER_OPERATION} операцию. Баланс карты - {balance}у.е.')