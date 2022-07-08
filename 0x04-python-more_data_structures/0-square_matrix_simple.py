#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    sqmat = []
    len_i = len(matrix)
    for i in range(0, len_i):
        for j in range(0, len(matrix[i])):
            sqmat[i][j] = matrix[i][j] * matrix[i][j]
    return sqmat
