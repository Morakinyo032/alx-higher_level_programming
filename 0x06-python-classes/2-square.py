#!/usr/bin/python3

"""Square class module"""


class Square:
    """Square class.

    Attributes:
        __size: Square size
    """

    def __init__(self, size=0):
        """Class magic method __init__ method

        Args:
            size: Size of Square object length

        Raises:
            TypeError:If size is not an integer.
            ValueError: If size is less than zero.

        """

        if type(size) is not int:
            raise TypeError("size must be an integer")       
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
