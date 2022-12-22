#!/usr/bin/python3
"""A square class"""


class Square:
    """Derives a square"""
    def __init__(self, size=0, position=(0, 0)):
        """Initialize attributes

        Args:
            self (int): value to initialize to `size`
            position (tuple): two positive integers

        Note:
            Do not include the `self` paramtere in the ``Args`` section.

        Raises:
            TypeError: when `size` isn't an integer
                       when `position` isn't a tuple of 2 integers
            ValueError: `size` is less than 0

        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

        if not isinstance(position, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        if len(position) != 2 or not all(isinstance(v, int) for v in position):
            raise TypeError("position must be a tuple of 2 positive integers")
        if not all(num >= 0 for num in position):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = position

    def area(self):
        """Calculate area of the square

        Returns:
            The area of the square

        """

        return self.__size ** 2

    @property
    def size(self):
        """Retrieves the value of `size`

        Returns:
            size
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Sets size to `value`

        Args:
            value (int): value to set set

        Raise:
            TypeError: if `value` isn't an integer
            ValueError: if `value` is less than 0

        """

        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    @property
    def position(self):
        """Retrieves `position` value """
        return self.__position

    @position.setter
    def position(self, value):
        """Sets the value of `position`
        Args:
            value (int): value to be set to `position` attribute
        Raise:
            TypeError: position isn't a tupple or doesn't contain 2
                       elements or has negative integers
        """

        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        if len(value) != 2 or not all(isinstance(v, int) for v in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        if not all(num >= 0 for num in value):
            raise TypeError("position must be a tuple of 2 positive integers")

        self.__position = value

    def my_print(self):
        """Print the square with the character `#`"""
        if self.__size > 0:
            [print() for i in range(self.__position[1])]
            for i in range(self.__size):
                print(" "*self.__position[0], end="")
                print("#"*self.__size)
        else:
            print()

    def __str__(self):
        """Print the square with the character `#`"""
        square = []

        if self.__size > 0:
            [square.append("\n") for i in range(self.__position[1])]
            for i in range(self.__size):
                for j in range(self.__position[0]):
                    square.append(" ")
                for k in range(self.__size):
                    square.append("#")
                if i < (self.__size - 1):
                    square.append("\n")
            return "".join(square)
        else:
            return ""
