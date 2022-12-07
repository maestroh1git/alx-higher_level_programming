#!/usr/bin/python3
def uniq_add(my_list=[]):
    if not my_list:
        pass

    s = set(my_list)
    n = 0

    for i in s:
        n += i
    return n
