#!/usr/bin/python3

"""Square class module"""


class Square:
    """Square class.

    Attributes:
        __size: Square size.
        __position: Shows the position of a Square object.
    """

    def __init__(self, size=0, position=(0, 0)):
        """Class magic method __init__ method.

        Args:
            size: Size of Square object length
            position: Position of the object

        Raises:
            TypeError:If size is not an integer or position is not a tuple.
            ValueError: If size is less than zero.

        """

        if type(size) is not int:
            raise TypeError("size must be an integer")       
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
            self.__position = position

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

    @property
    def position(self):
        """Getter that returns self.__position

        """

        return(self.__position)

    @position.setter
    def position(self, value):
        if type(value) is not tuple:
            raise TypeError("position must be a tuple of two positive integers")
        else:
            self.__position = value

    def area(self):
        """Instance method to return area of a Square object

        Returns:
            Returns the area of a Square object

        """

        return(self.__size ** 2)

    def my_print(self):
        """Prints the Square object with the character #."""

        if self.__size == 0:
            print("")
        else:
            for k in range(self.__position[1]):
                print("")
            for i in range(self.__size):
                for l in range(self.__position[0]):
                    print(" ", end='')
                for j in range(self.__size):
                    print("#", end='')
                print("")

    def __str__(self):
        l = []
        if self.__size == 0:
            return("")
        else:
            s = "\n" * (self.__position[1] - 1)
            l.append(s)
            t = " " * self.__position[0]
            u = "#" * self.__size
            v = t + u
            for i in range(self.__size):
                l.append(v)
            return("\n".join(l))

