#!/usr/bin/python3
"""
This is 2-matrix_divided module.
It contains the funtion matrix_divided().
"""


def matrix_divided(matrix, div):
    """"
    Divides all elements of a matrix by the number div.
    Returns a new matrix.
    """
    text = "matrix must be a matrix (list of lists) of integers/floats"
    for row in matrix:
        for element in row:
            if type(element) != int and type(element) != float:
                raise TypeError(text)
    for i in range(len(matrix)):
        if len(matrix[0]) != len(matrix[i]):
            raise TypeError("Each row of the matrix must be of the same size")
    if type(div) != int and type(div) != float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    new_matrix = []
    result = []
    for row in matrix:
        for i in range(len(row)):
            if row[i] % div == 0:
                a = float("{:.1f}".format(row[i] / div))
            else:
                a = float('{:.2f}'.format(row[i] / div))
            new_matrix.append(a)
        result.append(new_matrix)
        new_matrix = []
    return (result)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
