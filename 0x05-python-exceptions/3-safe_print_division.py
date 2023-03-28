#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        res = a / b
    except (ValueError, TypeError, ArithmeticError):
        f_res = "None"
        return (None)
    else:
        f_res = str(res)
        return (res)
    finally:
        print("Inside result: {}".format(f_res))
