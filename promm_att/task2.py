# Добавьте к ним логирование ошибок и полезной информации.
# Также реализуйте возможность запуска из командной строки с передачей параметров.
import logging
import argparse

logging.basicConfig(filename='info_task2.log', filemode='a', style='{', encoding='utf-8', level=logging.INFO)
logger = logging.getLogger(__name__)


def my_get(key, defolt_value=None):
    my_dict = {1: 'hello', 2: 'wrld'}
    res = defolt_value
    try:
        res = my_dict[key]
    except KeyError as e:
        logger.error(f'Ключа {key} не существует {e}')
    finally:
        logger.info(
            f'Функция: my_get(), словарь: {my_dict}, ключ: {key}, дефолтное значение: {defolt_value}, результат: {res}')
        return res


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Получаем начение по ключу',
        epilog='При отсутствии значения берем None',
        prog='my_get()'
    )
    parser.add_argument('-k', '--key', type=int, help='Ключ: ')
    parser.add_argument('-d', '--defolt_value', default=None, help='Дефолтное значение: ')
    args = parser.parse_args()
    print(my_get(args.key, args.defolt_value))
