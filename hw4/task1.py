# Напишите функцию для транспонирования матрицы

def transposed_matrix(matrix):
    res = []
    for i in range(len(matrix)):
        new_matrix = []
        for j in range(len(matrix[0])):
            new_matrix.append(matrix[j][i])
        res.append(new_matrix)
    return res


matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
print(transposed_matrix(matrix))