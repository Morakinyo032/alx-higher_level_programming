#!/usr/bin/python3

"""Square class module"""


class Square:
    """Square class.

    Attributes:
        __size: Square size
    """

    def __init__(self, size=0):
        """Class magic method __init__ method.

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

    @property
    def size(self):
        """Getter that returns self.__size.

        Args:
            value: Size of Square object length

        Raises:
            TypeError:If size is not an integer.
            ValueError: If size is less than zero.

        """

        return(self.__size)

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")       
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """Instance method to return area of a Square object

        Returns:
            Returns the area of a Square object

        """

        return(self.__size ** 2)

    def my_print(self):
        """Prints the Square object with the character #."""

        if self.__size is 0:
            print("")
        else:
            for i in range(self.__size):
                for j in range(self.__size):
                    print("#", end='')
                print("")
