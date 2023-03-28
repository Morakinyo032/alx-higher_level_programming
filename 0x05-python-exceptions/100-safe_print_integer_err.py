#!/usr/bin/python3
def safe_print_integer_err(value):
    import sys
    try:
        print("{:d}".format(value))
    except (ValueError, TypeError) as inst:
        sys.stderr.write("Exception: {}\n".format(inst.args[0]))
        return (False)
    else:
        return (True)
