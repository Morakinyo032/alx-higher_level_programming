#!/usr/bin/python3
"""
This is 4-print_square module which
contains the function print_square()
"""


def print_square(size):
    """Prints a square with the character #.
    size is the length of the square and must be a positive integer, else,
    an exception is raised.
    """
    if type(size) != int:
        if type(size) != float:
            if size < 0:
                raise TypeError("size must be an integer")
            else:
                size = int(size)
        else:
            raise TypeError("size must be an integer")
    else:
        if size < 0:
            raise ValueError("size must be >= 0")
    for i in range(size):
        for j in range(size):
            print("#", end='')
        print("")


if __name__ == "__main__":
    import doctest
    doctest.testmod()
