#!/usr/bin/python3


def safe_print_list(my_list=[], x=0):
    p = 0
    try:
        for p, e in enumerate(my_list[:x]):
            print("{}".format(e), end='')
        p = p + 1
        print()
    except:
        for p, e in enumerate(my_list[:]):
            print("{}".format(e), end='')
        p = p + 1
        print()
    finally:
        return p
