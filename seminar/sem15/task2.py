# На семинаре про декораторы был создан логирующий декоратор.
# Он сохранял аргументы функции и результат её работы в файл.
# Напишите аналогичный декоратор, но внутри используйте модуль logging.

# (Сама задача, кооторая была)
# Напишите декоратор, который сохраняет в json файл параметры декорируемой функции и результат, который она возвращает.
# При повторном вызове файл должен расширяться, а не перезаписываться.
# Каждый ключевой параметр сохраните как отдельный ключ json словаря.
# Для декорирования напишите функцию, которая может принимать как позиционные, так и ключевые аргументы.
# Имя файла должно совпадать с именем декорируемой функции.

from typing import Callable
import logging

logging.basicConfig(filename='info.log', filemode='a', encoding='utf-8', level=logging.INFO)
logger = logging.getLogger(__name__)


def my_logger(func: Callable):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        info_dict = {'arg': args, **kwargs, 'result': result}
        logger.info(info_dict)
        return result

    return wrapper


@my_logger
def get_all(num1, *args, **kwargs):
    return num1


if __name__ == '__main__':
    get_all(5, 34, 44, 'vfvf', a=12, b=32, c=34)
