#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    len_i = len(matrix)
    len_j = len(matrix[0])
    sqmat = []
    for i in range(0, len_i):
        pit = []
        for j in range(0, len_j):
            num = matrix[i][j] * matrix[i][j]
            pit.append(num)
        sqmat.append(pit)
    return sqmat
