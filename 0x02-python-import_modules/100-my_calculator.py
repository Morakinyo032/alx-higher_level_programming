#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, mul, div, sub
    from sys import exit, argv
    length = len(argv)
    flag = 0;
    if length != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        flag = 1
    else:
        a = int(argv[1])
        b = argv[2]
        c = int(argv[3])
        op = add
        operators = "+-/*"
        if b == '*':
            op = mul
        elif b == '-':
            op = sub
        elif b == '/':
            op = div
        elif b == '+':
            op = add
        if b not in operators:
            print("Unknown operator. Available operators: +, -, * and /")
            flag = 1;
        else:
            print("{:d} {} {:d} = {:d}".format(a, b, c, op(a, c)))
    if flag == 0:
        exit(0)
    else:
        exit(1)
