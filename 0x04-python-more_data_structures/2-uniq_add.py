#!/usr/bin/python3
def uniq_add(my_list=[]):
    new = list(set(my_list))
    list_sum = 0
    for x in new:
        list_sum += x
    return (list_sum)
