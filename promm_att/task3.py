# Добавьте к ним логирование ошибок и полезной информации.
# Также реализуйте возможность запуска из командной строки с передачей параметров.
import logging
import argparse

logging.basicConfig(filename='info_task3.log', filemode='a', style='{', encoding='utf-8', level=logging.INFO)
logger = logging.getLogger(__name__)


def tuple_file(inp_str):
    try:
        *a, b, c = inp_str.split('/')
    except ValueError as e:
        logger.error(f' В пути "{inp_str}" нет "/". {e}')
        logger.info(f' Путь: "{inp_str}", результат: {None}')
        return None

    try:
        name_file, file_extension = c.split('.')
    except ValueError as e:
        logger.error(f' В пути "{inp_str}" нет ".". {e}')
        logger.info(f' Путь: "{inp_str}", результат: {None}')
        return None

    res = (inp_str, name_file, file_extension)
    logger.info(f' Путь: "{inp_str}", результат: {res}')
    return res


if __name__ == '__main__':
    inp_str = 'D:Data/MyFile/sile.png'
    print(tuple_file(inp_str))
    parser = argparse.ArgumentParser(
        description='Получаем путь, имя файла, расширение файла',
        prog='tuple_file()'
    )
    parser.add_argument('-i', '--inp_str', type=str, help='Путь: ')
    args = parser.parse_args()
    print(tuple_file(args.inp_str))
