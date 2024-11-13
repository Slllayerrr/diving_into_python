#  модуль с проверкой даты добавьте возможность запуска в терминале с передачей даты на
# проверку.

from sys import argv


def is_leap(year: int) -> bool:  # проверка на високосность
    return year % 400 == 0 or year % 4 == 0 and year % 100 != 0


def is_valid_date(date: str = '21.11.2003') -> bool:
    day, month, year = map(int, date.split('.'))
    if year < 1 or year > 9999 or month < 1 or month > 12 or day < 1 or day > 31:
        return False
    else:
        if month in (4, 6, 9, 11):
            return day < 31
        if month == 2:
            if is_leap(year):
                return day < 30
            else:
                return day < 29


if __name__ == '__main__':
    params = argv[1:]
    # print(is_valid_date('29.02.2023'))
    print(is_valid_date(*params))
