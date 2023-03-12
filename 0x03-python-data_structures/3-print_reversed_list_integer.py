#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    a = len(my_list)
    for i in range(0, a):
        if type(my_list[i]) is int:
            print("{:d}".format(my_list[a - 1 - i]))
