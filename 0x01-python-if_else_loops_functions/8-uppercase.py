#!/usr/bin/python3
def uppercase(str):
    new_str = ""
    for i in range(len(str)):
        num = ord(str[i])
        c = str[i]
        if num >= 97 and num <= 122:
            num = num - 32
            new_str = new_str + chr(num)
        else:
            new_str = new_str + c
    print(new_str)
