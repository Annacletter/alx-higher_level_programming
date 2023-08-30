#!/usr/bin/python3
"""Creates a class Square"""


class Square:
    """Shows a square"""

    def __init__(self, size=0):
        """Initialize size"""
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """returns current Square area"""
        return self.__size * self.__size
