# Добавьте к ним логирование ошибок и полезной информации.
# Также реализуйте возможность запуска из командной строки с передачей параметров.
import logging
import argparse

logging.basicConfig(filename='info_task1.log', filemode='a', style='{', encoding='utf-8', level=logging.INFO)
logger = logging.getLogger(__name__)


def discriminant(a, b, c):
    try:
        d = b ** 2 - 4 * a * c
    except TypeError as e:
        logging.error(f'Не все параметры являются числом. {e}')
        logger.info(f'Функция: discriminant(), a: {a}, b: {b}, c: {c}, результат: {None}')
        return None
    if d > 0:
        x1 = (-b + d ** 0.5) / (2 * a)
        x2 = (-b - d ** 0.5) / (2 * a)
        res = f'{x1}, {x2}'
    elif d == 0:
        x = -b / (2 * a)
        res = f'{x}'
    else:
        x1 = (-b + d ** 0.5) / (2 * a)
        x2 = (-b - d ** 0.5) / (2 * a)
        res = f'{x1}, {x2}'

    logger.info(f'Функция: discriminant(), a: {a}, b: {b}, c: {c}, результат: {res}')

    return res


if __name__ == '__main__':
    print(discriminant(-1, 'jera', 8))
    print(discriminant(-1, 7, 8))

    parser = argparse.ArgumentParser(
        description='Получаем дискриминант',
        prog='discriminant()'
    )
    parser.add_argument('-a', '--a', type=float, help='Значение a: ')
    parser.add_argument('-b', '--b', type=float, help='Значение b: ')
    parser.add_argument('-c', '--c', type=float, help='Значение c: ')
    args = parser.parse_args()
    print(discriminant(args.a, args.b, args.c))
