#!/usr/bin/python3
"""
5-text_indentation module hich contains the function text_indentation()
"""


def text_indentation(text):
    """Prints a text with 2 lines after each characters: '.', '?', ':'.
    text must be a string else, an exception is raised.
    """
    if type(text) != str:
        raise TypeError("text must be a string")
    for i in range(len(text)):
        if i > 0:
            if text[i - 1] == '.' or text[i - 1] == '?' or text[i - 1] == ':':
                if text[i] == " ":
                    print("\n")
                else:
                    print("\n")
                    print(text[i], end="")
            else:
                print(text[i], end="")
        else:
            print(text[i], end="")
    print("")


if __name__ == "__main__":
    import doctest
    doctest.testmod()
