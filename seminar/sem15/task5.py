# Дорабатываем задачу 4.
# Добавьте возможность запуска из командной строки.
# При этом значение любого параметра можно опустить. В
# этом случае берётся первый в месяце день недели, текущий день недели и/или текущий месяц.
# *Научите функцию распознавать не только текстовое названия дня недели и месяца, но и числовые, т.е не мая, а 5.

import logging
from datetime import datetime as dt
import argparse

logging.basicConfig(filename='info_4.log', filemode='a', encoding='utf-8', level=logging.INFO)
logger = logging.getLogger(__name__)

MONTHS = ('', 'янв', 'фев', 'мар', 'апр', 'мая', 'июн', 'июл', 'авг', 'сен', 'окт', 'ноя', 'дек')
DAYS = ('пон', 'вто', 'сре', 'чет', 'пят', 'суб', 'вос')


def get_date(date: str):
    try:
        count, day, month = date.split()

    except ValueError as e:
        logging.error(f'Не смог разбить строку "{date}" на переменные {e}')
        return None

    count = int(count[0])
    day = int(day) if day.isdigit() else DAYS.index(day[:3])
    month = int(month) if month.isdigit() else MONTHS.index(month[:3])
    temp = 0
    for d in range(1, 32):
        date = dt(day=d, month=month, year=dt.now().year)
        if date.weekday() == day:
            temp +=1
            if temp == count:
                return date


def parse():
    parser = argparse.ArgumentParser(
        description='Получаем дату по дню недели и месяцу',
        epilog='При отсутствии значения берем текущий день недели и месяц',
        prog='get_date()'
    )
    parser.add_argument('-c','--count', default='1', help='Какой по счету день недели: ')
    parser.add_argument('-d','--day', default=dt.now().weekday(), help='Какой день недели: ')
    parser.add_argument('-m','--month', default=dt.now().month, help='Какой месяц: ')
    args = parser.parse_args()
    return get_date(f'{args.count} {args.day} {args.month}')

if __name__ == '__main__':
    print(get_date('1-й четверг ноября'))
    print(get_date('3-я среда мая'))
    print(get_date('1-йчетверг ноября'))
    print(parse())