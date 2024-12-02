# Создайте класс Матрица. Добавьте методы для:
# ○ вывода на печать,
# ○ сравнения,
# ○ сложения,
# ○ *умножения матриц

class Matrix:
    def __init__(self, rows: int, cols: int):
        self.rows = rows
        self.cols = cols
        self.data = [[0] * cols for _ in range(rows)]

    def __add__(self, other):
        data = []
        for i in range(0, len(self.data)):
            row_data = []
            for j in range(0, len(self.data[i])):
                sum = self.data[i][j] + other.data[i][j]
                row_data.append(sum)
            data.append(row_data)
        return data

    def __mul__(self, other):
        data = []
        for i in range(0, len(self.data)):
            row_data = []
            for j in range(0, len(self.data[i])):
                sum = self.data[i][j] * other.data[i][j]
                row_data.append(sum)
            data.append(row_data)
        return data

    def __str__(self):
        data_str = ''
        for i in range(0, len(self.data)):
            for j in range(0, len(self.data[i])):
                data_str += f'{self.data[i][j]} '
            if i != len(self.data) - 1:
                data_str += '\n'
        return data_str

    def __eq__(self, other):
        for i in range(0, len(self.data)):
            for j in range(0, len(self.data[i])):
                if self.data[i][j] != other.data[i][j]:
                    return False
                return True


if __name__ == '__main__':
    matrix1 = Matrix(2, 3)
    matrix1.data = [[1, 2, 3], [4, 5, 6]]
    matrix2 = Matrix(2, 3)
    matrix2.data = [[7, 8, 9], [10, 11, 12]]
    print(matrix1.data)
    print(matrix2.data)
    print(matrix1 + matrix2)
    print(matrix1 * matrix2)
    print(matrix1)
    print(matrix1 == matrix2)
