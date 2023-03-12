#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    new = list(a_dictionary.keys())
    new.sort()
    new_dict = {i: a_dictionary[i] for i in new}
    for key, value in new_dict.items():
        print("{}:".format(key), value)
