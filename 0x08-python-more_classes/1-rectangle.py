#!/usr/bin/python3
"""Shows a rectangle"""


class Rectangle:
    """Represents a rectangle"""

    def __init__(self, width=0, height=0):
        """Initializes the current rectangle.

        Args:
            width (int): width of the rectangle
            height (int): height of the rectangle
        """
        self.__width = 0  # Initialize width to 0
        self.__height = 0  # Initialize height to 0
        self.width = width  # Use the width property setter
        self.height = height  # Use the height property setter

    @property
    def width(self):
        """Get the width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get the height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
