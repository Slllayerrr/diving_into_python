# Напишите функцию, которая принимает количество дней от текущей даты и возвращает дату, которая наступит через указанное количество дней.
# Дополнительно, выведите эту дату в формате YYYY-MM-DD.
from datetime import timedelta, date


def get_date(count_day: int):
    date_now = date.today()
    print(date_now)
    dlt = timedelta(days=count_day)
    date_res = date_now + dlt
    return date_res.strftime('%Y-%m-%d')


if __name__ == '__main__':
    print(get_date(40))
