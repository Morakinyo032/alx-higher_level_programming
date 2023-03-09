#!/usr/bin/python3
from sys import argv
size = len(argv)
if size == 2:
    word = "argument:"
else:
    if size == 1:
        word = "arguments."
    else:
        word = "arguments:"
print("{:d} {}".format(size - 1, word))
for i in range(1, size):
    print("{:d}: {}".format(i, argv[i]))

if __name__ == "__main__":
    pass
