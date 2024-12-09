# Функция получает на вход текст вида: “1-й четверг ноября”, “3-я среда мая” и т.п.
# Преобразуйте его в дату в текущем году.
# Логируйте ошибки, если текст не соответсвует формату.
import logging
from datetime import datetime as dt

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
    day = DAYS.index(day[:3])
    month = MONTHS.index(month[:3])
    temp = 0
    for d in range(1, 32):
        date = dt(day=d, month=month, year=dt.now().year)
        if date.weekday() == day:
            temp +=1
            if temp == count:
                return date

if __name__ == '__main__':
    print(get_date('1-й четверг ноября'))
    print(get_date('3-я среда мая'))
    print(get_date('1-йчетверг ноября'))