#!/usr/bin/python3
"""
This is the "0-add_integer" module.

The module supplies one function, add_integer(). For example;
>>> add_integer(1, 5)
6
"""


def add_integer(a, b=98):
    """Addition of two integers
     If a or b is a float, it is casted into an integer.
    >>> add_integer(1, 6)
    7
    >>> add_integer(7.3, 6)
    13
    >>> add_integer(7.3, 8.8)
    15
    >>> add_integer(7.3, "school")
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
      File "<stdin>", line 9, in add_integer
    TypeError: b must be an integer
    >>> add_integer("school", 4)
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
      File "<stdin>", line 5, in add_integer
    TypeError: a must be an integer
    >>> add_integer(None)
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
      File "<stdin>", line 5, in add_integer
    TypeError: a must be an integer
    >>> add_integer(7.3, -8.8)
    -1
    >>> add_integer(-7.3, -8.8)
    -15  

	"""
    if type(a) == int or type(a) == float:
        x = int(a)
    else:
        raise TypeError("a must be an integer")
    if type(b) == int or type(b) == float:
        y = int(b)
    else:
        raise TypeError("b must be an integer")
    return (x + y)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
