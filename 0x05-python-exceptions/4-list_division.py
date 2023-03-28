#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    for i in range(list_length):
        try:
            val = my_list_1[i] / my_list_2[i]
            new_list.append(val)
        except ZeroDivisionError:
            print("division by 0")
            new_list.append(0)
        except TypeError:
            print("wrong type")
            new_list.append(0)
        except IndexError:
            print("out of range")
            new_list.append(0)
    try:
        list_length = len(new_list)
    except ValueError:
        pass
    finally:
        return (new_list)
