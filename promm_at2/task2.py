# Напишите скрипт, который получает текущее время и дату, а затем выводит их в
# формате YYYY-MM-DD HH:MM:SS. Дополнительно, выведите день недели и номер недели в году

from datetime import datetime


def get_date():
    date_now = datetime.now()
    print(date_now)
    date_week = date_now.strftime('%A')
    week_num = date_now.isocalendar()[1]
    return f'{date_now.strftime('%Y-%m-%d %H:%M:%S')=}, {date_week=}, {week_num=}'


if __name__ == '__main__':
    print(get_date())
