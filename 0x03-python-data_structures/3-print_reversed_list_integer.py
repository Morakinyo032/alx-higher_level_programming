#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if my_list == None:
        pass
    length = len(my_list)
    if length != 0:
        for i in range(length - 1, -1, -1):
            if type(my_list[i]) is int:
                print("{:d}".format(my_list[i]))
