#!/usr/bin/python3
def number_keys(a_dictionary):
    i = 0
    if not a_dictionary:
        pass
    for x, y in a_dictionary.items():
        i += 1
    return i
