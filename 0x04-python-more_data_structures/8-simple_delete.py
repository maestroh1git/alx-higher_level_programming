#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    if not a_dictionary or not key:
        pass
    else:
        for i, j in a_dictionary.items():
            if i == key:
                del a_dictionary[key]
                return a_dictionary
    return a_dictionary
