#!/usr/bin/python3
def main():
    pass


import sys, calculator_1 as cal
args = sys.argv
size = len(args)
if size != 4:
    print("Usage: ./100-my_calculator.py <a> <operator> <b>")
    sys.exit(1)
a = int(args[1])
b = int(args[3])
c = args[2]
flag = 0
if c == '+':
    print("{:d} + {:d} = {:d}".format(a, b, cal.add(a, b)))
elif c == '-':
    print("{:d} - {:d} = {:d}".format(a, b, cal.sub(a, b)))
elif c == '*':
    print("{:d} * {:d} = {:d}".format(a, b, cal.mul(a, b)))
elif c == '/':
    print("{:d} / {:d} = {:d}".format(a, b, cal.div(a, b)))
else:
    print("Unknown operator. Available operators: +, -, * and /")
    flag = 1
if __name__ == " __main__":
    main()
if flag == 0:
    sys.exit(0)
else:
    sys.exit(1)
