#!/usr/bin/python3
import hidden_4 as hid
names = dir(hid)
for i in names:
    if i[0] != '_' and i[1] != '_':
        print(i)

if __name__ == "__main__":
    pass
