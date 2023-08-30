#!/usr/bin/python3
class Square:
    """A class representing a square."""

    def __init__(self, size=0):
        """Initialize a Square instance.

        Args:
            size (int): The size of the square.
        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("Size must be an integer")
        if size < 0:
            raise ValueError("Size must be >= 0")

        self.__size = size
