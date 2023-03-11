#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix:
        for row in matrix:
            size = len(row)
            for i in range(size):
                print("{:d}".format(row[i]), end=' ' if i != size - 1 else '\n')
