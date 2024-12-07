import doctest


def my_get(my_dict, key, defolt_value=None):
    """
    >>> my_get({1: 'hello', 2: 'wrld'}, 5, 'Такого значения нет')
    'Такого значения нет'

    >>> my_get({1: 'hello', 2: 'wrld'}, 10)


    >>> my_get({1: 'hello', 2: 'wrld'}, 1)
    'hello'
    """
    res = defolt_value
    try:
        res = my_dict[key]
    except KeyError:
        pass
    return res

if __name__ == '__main__':
    doctest.testmod(verbose=True)