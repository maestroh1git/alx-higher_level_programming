#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    if not a_dictionary or not key or not value:
        pass

    a_dictionary[key] = value
    return a_dictionary
