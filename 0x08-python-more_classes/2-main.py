#!/usr/bin/python3
Rectangle = __import__('2-rectangle').Rectangle

my_rectangle = Rectangle(2, 4)
print("Area: {} - Perimeter: {}".format(my_rectangle.area(), my_rectangle.perimeter()))

print("--")

my_rectangle.width = 10
my_rectangle.height = 3
print(str(my_rectangle))
print(repr(my_rectangle))
print(my_rectangle)
print(repr(my_rectangle))
print("Area: {} - Perimeter: {}".format(my_rectangle.area(), my_rectangle.perimeter()))
