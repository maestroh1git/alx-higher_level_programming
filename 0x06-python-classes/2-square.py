#!/usr/bin/python3
"""A square class"""


class Square:
    """Derives a square"""
    def __init__(self, size=0):
        """Initialize attributes
        Args:
            self (int): value to initialize to `size`
        Note:
            Do not include the `self` parameter in the ``Args`` section.
        Raises:
            TypeError: when `size` isn't an integer
            ValueError: `size` is less than 0
        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
