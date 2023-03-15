#!/usr/bin/python3
def best_score(a_dictionary):
    length = 0
    if a_dictionary is not None:
        length = len(a_dictionary)
        if length == 0:
            return (None)
    elif a_dictionary is None:
        return (None)
    i = 0
    best = ''
    for x in a_dictionary.keys():
        i += 1
        if i == 1:
            best = x
        if a_dictionary[x] >= a_dictionary[best]:
            best = x
    return (best)
