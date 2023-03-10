#!/usr/bin/python3
def no_c(my_string):
    new = ''
    size = len(my_string)
    for i in range(size):
        if my_string[i] != chr(99) and my_string[i] != chr(67):
            new = new + my_string[i]
    return (new)
