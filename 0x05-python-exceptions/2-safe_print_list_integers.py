#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    pos = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            pos = pos + 1
        except (ValueError, TypeError):
            pass
    print("")
    return (pos)
