#!/usr/bin/python3
def remove_char_at(str, n):
    size = len(str)
    new_str = ""
    for i in range(size):
        num = ord(str[i])
        c = str[i]
        if i == n:
            pass
        else:
            new_str = new_str + c
    return (new_str)
