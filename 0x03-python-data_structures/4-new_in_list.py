#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    new = [] + my_list
    size = len(my_list)
    if idx < 0 or idx >= size:
        return (new)
    new[idx] = element
    return (new)
