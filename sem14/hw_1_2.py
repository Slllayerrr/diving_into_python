# ○ unittest
import unittest


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


class TestCaseName(unittest.TestCase):
    def test_two_root(self):
        self.assertEqual('-1.0, 8.0', discriminant(-1, 7, 8))

    def test_one_root(self):
        self.assertEqual('-0.5', discriminant(4, 4, 1))

    def test_two_compl_root(self):
        self.assertEqual('(-0.24999999999999997+0.6614378277661477j), (-0.25000000000000006-0.6614378277661477j)',
                         discriminant(2, 1, 1))


if __name__ == '__main__':
    unittest.main(verbosity=2)
