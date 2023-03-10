#!/usr/bin/python3
def mod_2(t=()):
    size = len(t)
    new = []
    if size > 2:
        new = [t[0], t[1]]
    elif size < 2:
        if size == 1:
            new = [t[0], 0]
        else:
            new = [0, 0]
    else:
        return (t)
    return (tuple(new))


def add_tuple(tuple_a=(), tuple_b=()):
    size1 = len(tuple_a)
    size2 = len(tuple_b)
    if size1 != 2:
        tuple_a = mod_2(tuple_a)
    if size2 != 2:
        tuple_b = mod_2(tuple_b)
    a = tuple_a[0] + tuple_b[0]
    b = tuple_a[1] + tuple_b[1]
    new = [a, b]
    return (tuple(new))
