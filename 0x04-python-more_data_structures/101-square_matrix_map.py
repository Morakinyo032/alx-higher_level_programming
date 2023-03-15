#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    return (list(map(lambda i: list(map(lambda j: matrix[i][j]**2, range(len(matrix[i])))), range(len(matrix)))))
