#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    pos = 0
    try:
        for i in range(x):
            print(my_list[i], end='')
            pos = pos + 1
    except IndexError:
        pass
    print("")
    return (pos)
