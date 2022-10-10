#!/usr/bin/python3


def safe_print_list(my_list=[], x=0):
    len_list = 0
    for i in range(0, x):
        try:
            print(my_list[i], end="")
            len_list += 1
        except IndexError:
            pass
    print("")
    return len_list
