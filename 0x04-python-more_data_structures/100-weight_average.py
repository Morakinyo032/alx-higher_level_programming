#!/usr/bin/python3
def weight_average(my_list=[]):
    length = len(my_list)
    if length == 0:
        return (0)
    Total = 0
    freq = 0
    for x in my_list:
        Total += x[0] * x[1]
        freq += x[1]
    return (Total / freq)
