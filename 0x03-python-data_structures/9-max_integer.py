#!/usr/bin/python3
def max_integer(my_list=[]):
    size = len(my_list)
    if size == 0:
        return (None)
    x = my_list[0]
    for i in my_list:
        if x < i:
            x = i
    return (x)
