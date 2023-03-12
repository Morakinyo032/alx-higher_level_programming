#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
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
