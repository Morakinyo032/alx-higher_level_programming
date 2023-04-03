#!/usr/bin/python3
"""Module that contains the class Rectangle"""

class Rectangle:
    """ Class Rectangle

    """
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """__init__ method

        """
        self.__width = width
        self.__height = height
        Rectangle.number_of_instances += 1


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
        new = []
        for i in range(self.__height):
            for j in range(self.__width):
                new.append(self.print_symbol)
            if i < self.__height - 1:
                new.append('\n')
        my_str = ''.join(map(str, new))
        return (my_str)


    def __repr__(self):
        """repr() method.

        """

        return (f"Rectangle({self.__width}, {self.__height})")


    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1


    @staticmethod
    def bigger_or_equal(rec_1, rec_2):
        if type(rec_1) is not Rectangle:
            raise TypeError('rec_1 must be  an instance of Rectangle')
        if type(rec_2) is not Rectangle:
            raise TypeError('rec_2 must be  an instance of Rectangle')
        if rec_1.area() < rec_2.area():
            return (rec_2)
        elif rec_1.area() > rec_2.area():
            return (rec_1)
        else:
            return (rec_1)
