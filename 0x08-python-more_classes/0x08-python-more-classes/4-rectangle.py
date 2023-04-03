#!/usr/bin/python3
"""Module that contains the class Rectangle"""

class Rectangle:
    """ Class Rectangle

    """

    def __init__(self, width=0, height=0):
        """__init__ method

        """
        self.__width = width
        self.__height = height


    @property
    def width(self):
        return (self.__width)


    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value


    @property
    def height(self):
        return (self.__height)


    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value


    def area(self):
        """Instance method area.

        Return: The area of the instance.

        """

        return (self.__width * self.__height)


    def perimeter(self):
        """ Instance method perimeter.

        Return: The perimeter of a Rectangle instance.

        """

        if self.__width == 0 or self.__height == 0:
            return (0)
        return (2 * (self.__height + self.__width))


    def __str__(self):
        """str() method.

        """
        strl = list(map(lambda x: '#' * self.__width, range(self.__height)))
        return ('\n'.join(strl))


    def __repr__(self):
        """repr() method.

        """

        return (f"Rectangle({self.__width}, {self.__height})")
