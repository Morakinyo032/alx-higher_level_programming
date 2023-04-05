#!/usr/bin/python3
"""Matrix multiplication
"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """
    Multiplies two matrices and return their product.
    """
    if type(m_a) != list:
        raise TypeError("m_a must be a list")
    if type(m_b) != list:
        raise TypeError("m_b must be a list")
    for row in m_a:
        if type(row) != list:
            raise TypeError("m_a must be a list of lists")
    for row in m_b:
        if type(row) != list:
            raise TypeError("m_b must be a list of lists")
    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")
    for row in m_a:
        for element in row:
            if type(element) not in [int, float]:
                raise TypeError("m_a should contain only integers or floats")
    for row in m_b:
        for element in row:
            if type(element) not in [int, float]:
                raise TypeError("m_b should contain only integers or floats")
    for i in range(len(m_a)):
        if len(m_a[0]) != len(m_a[i]):
            raise TypeError("each row of m_a must be of the same size")
    for i in range(len(m_b)):
        if len(m_b[0]) != len(m_b[i]):
            raise TypeError("each row of m_b must be of the same size")
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_ and m_b can't be multiplied")
    a, b = np.array(m_a), np.array(m_b)
    return (a @ b)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
