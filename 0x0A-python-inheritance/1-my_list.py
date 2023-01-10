#!/usr/bin/python3
"""
Defines the MyList class
"""


class MyList(list):
    """subclass of list"""
    def print_sorted(self):
        """prints the sorted list"""
        print(sorted(self))
