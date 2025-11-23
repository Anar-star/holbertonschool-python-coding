#!/usr/bin/python3
"""Module that defines a Square class with size and printing capabilities"""


class Square:
    """Class that defines a square with size, area, and printing"""

    def __init__(self, size=0):
        """Initialize the square with validated size"""
        self.size = size  # Use the setter for validation

    @property
    def size(self):
        """Retrieve the private size attribute"""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the private size attribute with validation"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the current square area"""
        return self.__size ** 2

    def my_print(self):
        """Print the square with the character #"""
        if self.__size == 0:
            print()
            return
        for _ in range(self.__size):
            print("#" * self.__size)
