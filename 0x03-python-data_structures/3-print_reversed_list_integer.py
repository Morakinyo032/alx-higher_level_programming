#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    a = len(my_list)
    if a == 0:
        pass
    else:
        for i in range(0, a):
            print("{:d}".format(my_list[a - 1 - i]))
