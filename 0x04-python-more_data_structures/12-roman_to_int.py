#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None or type(roman_string) is not str:
        return (0)
    numerals = "IVLXDMC"
    length = len(roman_string)
    for k in range(length):
        if roman_string[k] not in numerals:
            return (0)
    if length > 3:
        for j in range(length):
            ch = roman_string[j]
            if j + 3 <= length - 1:
                if roman_string[j + 1] == ch:
                    if roman_string[j + 2] == ch:
                        if roman_string[j + 3] == ch:
                            print("Wrong numeral combination-> ", end='')
                            return (0)
            else:
                break
    dic = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    result = 0
    if length == 1:
        return (dic[roman_string[0]])
    for i in range(length):
        first = roman_string[i]
        if i + 1 <= length - 1:
            if dic[first] < dic[roman_string[i + 1]]:
                result -= dic[first]
            else:
                result += dic[first]
        else:
            result += dic[first]
    return (result)
