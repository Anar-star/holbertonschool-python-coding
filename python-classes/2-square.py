#!/usr/bin/python3
"""Module that defines a Square class with area calculation"""


class Square:
    """Class that defines a square with size and area"""

    def __init__(self, size=0):
        """Initialize the square with size and validate it"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Return the current square area"""
        return self.__size ** 2
