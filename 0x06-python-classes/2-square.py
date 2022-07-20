#!/usr/bin/python3
"""A module
"""


class Square:
    """Class square that defines a square by size and contains exceptions
    """
    def __init__(self, size=0):
        """Initialize data and raise exceptions
        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
