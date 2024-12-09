# ○ pytest
import pytest


def discriminant(a, b, c):
    d = b ** 2 - 4 * a * c
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

    return res


def test_original_str():
    assert discriminant(-1, 7, 8) == '-1.0, 8.0'


def test_lower():
    assert discriminant(4, 4, 1) == '-0.5'


def test_punctuation():
    assert discriminant(2, 1,1) == '(-0.24999999999999997+0.6614378277661477j), (-0.25000000000000006-0.6614378277661477j)'


if __name__ == '__main__':
    pytest.main(['-vv'])