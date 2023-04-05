#!/usr/bin/python3
"""
This is 3-say_my_name module.
It contains the functions say_my_name(), e.g;
>>> say_my_name("John", "Smith")
My name is John Smith
"""


def say_my_name(first_name, last_name=""):
    """
    Prints "My name is <first_name> <last_name>"
    first_name and last_name must be strings else an exception is raised.
    """
    if type(first_name) != str:
        raise TypeError("first_name must be a string")
    if type(last_name) != str:
        raise TypeError("last_name must be a string")
    if len(first_name) == 0 or len(last_name) == 0:
        pass
    print("My name is {} {}".format(first_name, last_name))


if __name__ == "__main__":
    import doctest
    doctest.testmod()
