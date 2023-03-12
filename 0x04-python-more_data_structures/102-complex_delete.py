#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    length = len(a_dictionary)
    for i in range(length):
        for x in a_dictionary:
            if a_dictionary[x] == value:
                del (a_dictionary[x])
                break
            i += 1
    return (a_dictionary)
