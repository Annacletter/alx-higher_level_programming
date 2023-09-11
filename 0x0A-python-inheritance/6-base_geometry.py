#!/usr/bin/python3
"""Shows class BaseGeometry with a public instance method"""


class BaseGeometry:
    """Represents base geometry"""
    def area(self):
        """Is not implemented"""
        raise Exception("area() is not implemented")
