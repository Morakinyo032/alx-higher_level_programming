#!/usr/bin/python3
def safe_function(fct, *args):
    import sys
    try:
        res = fct(*args)
    except (ArithmeticError, IndexError, ValueError) as inst:
        sys.stderr.write("Exception: {}\n".format(inst.args[0]))
        return (None)
    else:
        return (res)
