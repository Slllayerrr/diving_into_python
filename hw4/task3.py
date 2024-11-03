# Возьмите задачу о банкомате из семинара 2. Разбейте её на отдельные операции — функции.
# Дополнительно сохраняйте все операции поступления и снятия средств в список.
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
PRECENT_BONUS = decimal.Decimal(3 / decimal.Decimal(100))

balance = decimal.Decimal(0)
count = 0
lst_oper = []

def  choice_oper():
    action = input(f'Пополнить - "{CMD_DEPOSIT}", Снять - "{CMD_WITHDRAW}", Выйти - "{CMD_EXIT}": ')
    return action

def act_exit(balance):
    print(f'Заберите карту. Баланс: {balance}у.е')
    return balance

def balance_more_rich(balance):
    present = balance * PRECENT_RICHNESS
    balance -= present
    print(f'Вычтен налог на богатство {PRECENT_RICHNESS * 100}%.'
          f'Сумма процента - {present}. Баланс карты - {balance}у.е.')
    return balance

def act_depos(balance, count):
    balance += amount
    count += 1
    print(f'Зачислено {amount}у.е. Баланс карты - {balance}у.е.')
    lst_oper.append(f'зачислено: {amount}')
    return balance, count, lst_oper

def act_with(balance, count):
    precent = amount * PRECENT_WITHDRAWAL
    precent = MIN_REMOVAL if precent < MIN_REMOVAL else MAX_REMOVAL if precent > MAX_REMOVAL else precent
    sub = amount + precent
    if balance > sub:
        balance -= sub
        count += 1
        lst_oper.append(f'снято: {amount}')
        print(f'Снятие с карты {amount}у.е. Сумма процента за снятие {precent}. Баланс карты {balance}.')
    else:
        print(
            f'Недостаточно средств. Сумма снятия {amount}у.е. Сумма процента за снятие {precent}. Баланс карты {balance}.')
    return balance, count, lst_oper

def bonus_count(balance):
    bonus = balance * PRECENT_BONUS
    balance += bonus
    print(f'Начислен бонус {bonus} за каждую {NUMBER_OPERATION} операцию. Баланс карты - {balance}у.е.')
    return balance


while True:
    oper = choice_oper()
    if oper == CMD_EXIT:
        act_exit(balance)
        break
    if balance > RICHNESS_SUM:
        balance = balance_more_rich(balance)
    if oper in (CMD_DEPOSIT, CMD_WITHDRAW):
        amount = 1
        while amount % MULTIPLISITY != 0:
            amount = decimal.Decimal(input(f'Введите сумму кратную {MULTIPLISITY}: '))
        if oper == CMD_DEPOSIT:
            balance, count, lst_oper = act_depos(balance, count)
        elif oper == CMD_WITHDRAW:
            balance, count, lst_oper = act_with(balance, count)
    if count % NUMBER_OPERATION == 0 and count != 0:
        balance = bonus_count(balance)
print(lst_oper)