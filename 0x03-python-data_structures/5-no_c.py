#!/usr/bin/python3
def no_c(my_string):
    new_str = my_string
    for ch in my_string:
        if ch == 'c' or ch == 'C':
            new_str = new_str.translate({ord(ch): None})
    return new_str
