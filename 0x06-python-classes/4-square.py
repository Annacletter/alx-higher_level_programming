#!/usr/bin/python3
"""Creates class Square"""


class Square:
    """Shows a square"""

    def __init__(self, size=0):
        """Initialize size"""
        self.size = size

    @property
    def size(self):
        """gets and sets the current size"""
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """returns the current Square area"""
        return self.__size * self.__size
