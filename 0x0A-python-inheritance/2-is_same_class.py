#!/usr/bin/python3
"""Shows class checking function"""


def is_same_class(obj, a_class):
    """Checks object if its an instance of the specified class.
    """
    if type(obj) is a_class:
        return True
    return False
