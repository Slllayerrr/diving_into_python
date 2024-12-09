# Доработаем задачу 2.
# Сохраняйте в лог файл раздельно:
# ○ уровень логирования,
# ○ дату события,
# ○ имя функции (не декоратора),
# ○ аргументы вызова,
# ○ результат.

from typing import Callable
import logging

FORMAT = '{levelname:<8} - {asctime}. {msg}'
logging.basicConfig(filename='info.log', filemode='a', style='{', format=FORMAT, encoding='utf-8', level=logging.INFO)
logger = logging.getLogger(__name__)


def my_logger(func: Callable):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        info_dict = {'arg': args, **kwargs, 'result': result}
        logger.info(f'Функция: {func.__name__}(), аргументы: {info_dict}, результат: {result}')
        return result

    return wrapper


@my_logger
def get_all(num1, *args, **kwargs):
    return num1


if __name__ == '__main__':
    get_all(5, 34, 44, 'vfvf', a=12, b=32, c=34)
