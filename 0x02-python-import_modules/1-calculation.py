#!/usr/bin/python3
add = __import__('calculation_1').add
sub = __import__('calculation_1').sub
mul = __import__('calculation_1').mul
div = __import__('calculation_1').div
a = 10
b = 5
print("{:d} + {:d} = {:d}".format(a, b, add(a, b)))
print("{:d} - {:d} = {:d}".format(a, b, sub(a, b)))
print("{:d} * {:d} = {:d}".format(a, b, mul(a, b)))
print("{:d} / {:d} = {:d}".format(a, b, div(a, b)))

if __name__ == "__main__":
    pass
